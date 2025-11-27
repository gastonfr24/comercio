"""
Script to create a default superuser for development.

Credentials are loaded from environment variables for security.
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Get credentials from environment variables
username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not password:
    print("ERROR: DJANGO_SUPERUSER_PASSWORD environment variable is not set!")
    print("Please set it in your .env.dev file")
    exit(1)

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser "{username}" created successfully!')
    print(f"Username: {username}")
    print(f"Email: {email}")
    print("Password: (from environment variable)")
else:
    print(f'Superuser "{username}" already exists.')
