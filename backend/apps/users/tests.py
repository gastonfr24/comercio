"""
Tests for users app models and permissions.
"""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView
from .permissions import IsAdmin, IsCashier, IsAdminOrCashier, IsAdminOrReadOnly

User = get_user_model()

# Test password constant (not a real secret, only for testing)
TEST_PASSWORD = "test_password_for_unit_tests_only"


@pytest.mark.django_db
class TestUserModel:
    """
    Tests for custom User model.
    """

    def test_create_user_default_role(self):
        """
        Test creating user with default role (CASHIER).
        """
        user = User.objects.create_user(
            username="testuser", email="test@example.com", password=TEST_PASSWORD
        )

        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.role == User.Role.CASHIER
        assert user.is_cashier is True
        assert user.is_admin is False

    def test_create_admin_user(self):
        """
        Test creating user with ADMIN role.
        """
        user = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password=TEST_PASSWORD,
            role=User.Role.ADMIN,
        )

        assert user.role == User.Role.ADMIN
        assert user.is_admin is True
        assert user.is_cashier is False

    def test_user_str_representation(self):
        """
        Test string representation of User.
        """
        user = User.objects.create_user(
            username="testuser", role=User.Role.CASHIER, password=TEST_PASSWORD
        )

        assert str(user) == "testuser (Cashier)"

    def test_admin_user_str_representation(self):
        """
        Test string representation of admin user.
        """
        user = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )

        assert str(user) == "admin (Administrator)"

    def test_has_admin_permissions(self):
        """
        Test has_admin_permissions method.
        """
        admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )

        assert admin.has_admin_permissions() is True
        assert cashier.has_admin_permissions() is False

    def test_superuser_has_admin_permissions(self):
        """
        Test that superuser has admin permissions regardless of role.
        """
        superuser = User.objects.create_superuser(
            username="super",
            email="super@example.com",
            password=TEST_PASSWORD,
            role=User.Role.CASHIER,
        )

        assert superuser.has_admin_permissions() is True

    def test_can_manage_products(self):
        """
        Test can_manage_products permission.
        """
        admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )

        assert admin.can_manage_products() is True
        assert cashier.can_manage_products() is False

    def test_can_manage_users(self):
        """
        Test can_manage_users permission.
        """
        admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )

        assert admin.can_manage_users() is True
        assert cashier.can_manage_users() is False

    def test_can_view_reports(self):
        """
        Test can_view_reports permission.
        """
        admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )

        assert admin.can_view_reports() is True
        assert cashier.can_view_reports() is False

    def test_can_manage_cash_register(self):
        """
        Test can_manage_cash_register permission.
        """
        admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )
        inactive = User.objects.create_user(
            username="inactive", role=User.Role.CASHIER, password=TEST_PASSWORD, is_active=False
        )

        assert admin.can_manage_cash_register() is True
        assert cashier.can_manage_cash_register() is True
        assert inactive.can_manage_cash_register() is False

    def test_can_make_sales(self):
        """
        Test can_make_sales permission.
        """
        admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )
        inactive = User.objects.create_user(
            username="inactive", role=User.Role.CASHIER, password=TEST_PASSWORD, is_active=False
        )

        assert admin.can_make_sales() is True
        assert cashier.can_make_sales() is True
        assert inactive.can_make_sales() is False

    def test_user_with_phone(self):
        """
        Test creating user with phone number.
        """
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password=TEST_PASSWORD,
            phone="+1234567890",
        )

        assert user.phone == "+1234567890"


@pytest.mark.django_db
class TestPermissions:
    """
    Tests for custom permission classes.
    """

    def setup_method(self):
        """
        Set up test fixtures.
        """
        self.factory = APIRequestFactory()
        self.view = APIView()

        self.admin = User.objects.create_user(
            username="admin", role=User.Role.ADMIN, password=TEST_PASSWORD
        )
        self.cashier = User.objects.create_user(
            username="cashier", role=User.Role.CASHIER, password=TEST_PASSWORD
        )

    def test_is_admin_permission_allows_admin(self):
        """
        Test IsAdmin permission allows admin users.
        """
        request = self.factory.get("/")
        request.user = self.admin

        permission = IsAdmin()
        assert permission.has_permission(request, self.view) is True

    def test_is_admin_permission_denies_cashier(self):
        """
        Test IsAdmin permission denies cashier users.
        """
        request = self.factory.get("/")
        request.user = self.cashier

        permission = IsAdmin()
        assert permission.has_permission(request, self.view) is False

    def test_is_cashier_permission_allows_cashier(self):
        """
        Test IsCashier permission allows cashier users.
        """
        request = self.factory.get("/")
        request.user = self.cashier

        permission = IsCashier()
        assert permission.has_permission(request, self.view) is True

    def test_is_cashier_permission_denies_admin(self):
        """
        Test IsCashier permission denies admin users.
        """
        request = self.factory.get("/")
        request.user = self.admin

        permission = IsCashier()
        assert permission.has_permission(request, self.view) is False

    def test_is_admin_or_cashier_allows_admin(self):
        """
        Test IsAdminOrCashier permission allows admin.
        """
        request = self.factory.get("/")
        request.user = self.admin

        permission = IsAdminOrCashier()
        assert permission.has_permission(request, self.view) is True

    def test_is_admin_or_cashier_allows_cashier(self):
        """
        Test IsAdminOrCashier permission allows cashier.
        """
        request = self.factory.get("/")
        request.user = self.cashier

        permission = IsAdminOrCashier()
        assert permission.has_permission(request, self.view) is True

    def test_is_admin_or_read_only_allows_admin_write(self):
        """
        Test IsAdminOrReadOnly allows admin to write.
        """
        request = self.factory.post("/")
        request.user = self.admin

        permission = IsAdminOrReadOnly()
        assert permission.has_permission(request, self.view) is True

    def test_is_admin_or_read_only_allows_cashier_read(self):
        """
        Test IsAdminOrReadOnly allows cashier to read.
        """
        request = self.factory.get("/")
        request.user = self.cashier

        permission = IsAdminOrReadOnly()
        assert permission.has_permission(request, self.view) is True

    def test_is_admin_or_read_only_denies_cashier_write(self):
        """
        Test IsAdminOrReadOnly denies cashier write access.
        """
        request = self.factory.post("/")
        request.user = self.cashier

        permission = IsAdminOrReadOnly()
        assert permission.has_permission(request, self.view) is False

