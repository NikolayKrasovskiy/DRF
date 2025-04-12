from django.urls import path
from .views import AdvertisementViewSet  # Предполагая, что у вас ViewSet

urlpatterns = [
    path('advertisements/', AdvertisementViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('advertisements/<int:pk>/', AdvertisementViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]
