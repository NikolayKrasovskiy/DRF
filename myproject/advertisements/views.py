from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly


def home(request):
    """
    Представление для отображения главной страницы.
    """
    return render(request, 'my_template.html')


class AdvertisementViewSet(viewsets.ModelViewSet):
    """
    ViewSet для объявлений.
    """
    queryset = Advertisement.objects.all().order_by('created_at')
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = [permissions.AllowAny] # Права доступа по умолчанию

    def get_permissions(self):
        """
        Определяет права доступа в зависимости от действия.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Для создания, обновления, частичного обновления и удаления требуется аутентификация и быть владельцем.
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            # Для остальных действий (например, list, retrieve) разрешено всем.
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Сохраняет объявление, устанавливая создателя и проверяя лимит открытых объявлений.
        """
        # Проверяем, не превышает ли пользователь лимит в 10 открытых объявлений.
        if Advertisement.objects.filter(creator=self.request.user, status='OPEN').count() >= 10:
            raise serializers.ValidationError("You cannot have more than 10 open advertisements.")
        # Сохраняем объявление, устанавливая текущего пользователя как создателя.
        serializer.save(creator=self.request.user)
