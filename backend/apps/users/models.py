"""
User model with role-based access control.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser with role support.

    Attributes:
        role: User role (ADMIN or CASHIER)
        phone: Optional phone number
        is_active: Whether the user account is active
    """

    class Role(models.TextChoices):
        """
        User role choices.
        """

        ADMIN = "ADMIN", "Administrator"
        CASHIER = "CASHIER", "Cashier"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CASHIER,
        help_text="User role for permissions",
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Phone number (optional)",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
        indexes = [
            models.Index(fields=["role"]),
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        """
        String representation of User.

        Returns:
            Username and role
        """
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_admin(self):
        """
        Check if user is an administrator.

        Returns:
            True if user has ADMIN role

        Example:
            >>> user.is_admin
            True
        """
        return self.role == self.Role.ADMIN

    @property
    def is_cashier(self):
        """
        Check if user is a cashier.

        Returns:
            True if user has CASHIER role

        Example:
            >>> user.is_cashier
            True
        """
        return self.role == self.Role.CASHIER

    def has_admin_permissions(self):
        """
        Check if user has admin permissions.

        Returns:
            True if user is superuser or has ADMIN role
        """
        return self.is_superuser or self.is_admin

    def can_manage_products(self):
        """
        Check if user can manage products.

        Returns:
            True if user has admin permissions
        """
        return self.has_admin_permissions()

    def can_manage_users(self):
        """
        Check if user can manage other users.

        Returns:
            True if user has admin permissions
        """
        return self.has_admin_permissions()

    def can_view_reports(self):
        """
        Check if user can view reports and analytics.

        Returns:
            True if user has admin permissions
        """
        return self.has_admin_permissions()

    def can_manage_cash_register(self):
        """
        Check if user can open/close cash register.

        Returns:
            True for both admins and cashiers
        """
        return self.is_active and (self.is_admin or self.is_cashier)

    def can_make_sales(self):
        """
        Check if user can make sales.

        Returns:
            True for both admins and cashiers
        """
        return self.is_active and (self.is_admin or self.is_cashier)

