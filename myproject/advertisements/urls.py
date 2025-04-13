from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet, home  # Импортируем представление home

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = [
    path('', home, name='home'),  # Маршрут для главной страницы
    path('api/', include(router.urls)),  # Маршрут для API
]
