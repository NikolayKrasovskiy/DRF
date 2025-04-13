from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('advertisements.urls')),  # Включение маршрутов приложения
    path('', include('advertisements.urls')),  # Маршрут для главной страницы
]
