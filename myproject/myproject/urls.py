from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('advertisements.urls')),  # Предполагая, что у вас есть app 'advertisements'
    path('', include('advertisements.urls')),  # Маршрут для главной страницы (если он существует в вашем app)
]
