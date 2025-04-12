import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Создание суперпользователя
User.objects.create_superuser('admin', 'admin@example.com', 'admin12345678')
print("Superuser created successfully.")
