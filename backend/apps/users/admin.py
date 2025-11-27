"""
Django admin configuration for users app.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin configuration for User model.
    """

    list_display = [
        "username",
        "email",
        "role",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
    ]

    list_filter = [
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    ]

    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
    ]

    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Role & Permissions",
            {
                "fields": ("role",),
            },
        ),
        (
            "Contact Information",
            {
                "fields": ("phone",),
            },
        ),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            "Role",
            {
                "fields": ("role",),
            },
        ),
    )

    ordering = ["-date_joined"]

