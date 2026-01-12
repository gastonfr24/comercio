"""
Custom permission classes for role-based access control.
"""

from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Permission class that allows only users with ADMIN role.
    """

    message = "Only administrators can perform this action."

    def has_permission(self, request, view):
        """
        Check if user is authenticated and has ADMIN role.

        Args:
            request: Django request object
            view: View being accessed

        Returns:
            True if user is admin, False otherwise
        """
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "is_admin")
            and request.user.is_admin
        )


class IsCashier(permissions.BasePermission):
    """
    Permission class that allows only users with CASHIER role.
    """

    message = "Only cashiers can perform this action."

    def has_permission(self, request, view):
        """
        Check if user is authenticated and has CASHIER role.

        Args:
            request: Django request object
            view: View being accessed

        Returns:
            True if user is cashier, False otherwise
        """
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "is_cashier")
            and request.user.is_cashier
        )


class IsAdminOrCashier(permissions.BasePermission):
    """
    Permission class that allows users with ADMIN or CASHIER role.
    """

    message = "Only administrators or cashiers can perform this action."

    def has_permission(self, request, view):
        """
        Check if user is authenticated and has ADMIN or CASHIER role.

        Args:
            request: Django request object
            view: View being accessed

        Returns:
            True if user is admin or cashier, False otherwise
        """
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "role")
            and (request.user.is_admin or request.user.is_cashier)
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class that allows full access to admins and read-only to others.
    """

    message = "Only administrators can modify this resource."

    def has_permission(self, request, view):
        """
        Check permissions based on request method.

        Args:
            request: Django request object
            view: View being accessed

        Returns:
            True if user can access, False otherwise
        """
        # Read permissions for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Write permissions only for admins
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, "is_admin")
            and request.user.is_admin
        )

