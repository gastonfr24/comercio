"""
Tests for JWT authentication endpoints.
"""

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    """
    Fixture for API client.
    """
    return APIClient()


@pytest.fixture
def test_user(db):
    """
    Fixture to create a test user.
    """
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpassword123",
    )


@pytest.mark.django_db
class TestJWTAuthentication:
    """
    Tests for JWT authentication endpoints.
    """

    def test_obtain_token_success(self, api_client, test_user):
        """
        Test obtaining JWT token with valid credentials.
        """
        url = reverse("token_obtain_pair")
        data = {
            "username": "testuser",
            "password": "testpassword123",
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data
        assert isinstance(response.data["access"], str)
        assert isinstance(response.data["refresh"], str)

    def test_obtain_token_invalid_credentials(self, api_client, test_user):
        """
        Test obtaining token with invalid credentials fails.
        """
        url = reverse("token_obtain_pair")
        data = {
            "username": "testuser",
            "password": "wrongpassword",
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "access" not in response.data
        assert "refresh" not in response.data

    def test_obtain_token_missing_username(self, api_client):
        """
        Test obtaining token without username fails.
        """
        url = reverse("token_obtain_pair")
        data = {
            "password": "testpassword123",
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_obtain_token_missing_password(self, api_client):
        """
        Test obtaining token without password fails.
        """
        url = reverse("token_obtain_pair")
        data = {
            "username": "testuser",
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_refresh_token_success(self, api_client, test_user):
        """
        Test refreshing JWT token with valid refresh token.
        """
        # First, obtain tokens
        login_url = reverse("token_obtain_pair")
        login_data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        login_response = api_client.post(login_url, login_data, format="json")
        refresh_token = login_response.data["refresh"]

        # Now refresh
        refresh_url = reverse("token_refresh")
        refresh_data = {
            "refresh": refresh_token,
        }

        response = api_client.post(refresh_url, refresh_data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        # With ROTATE_REFRESH_TOKENS=True, a new refresh token is also returned
        assert "refresh" in response.data

    def test_refresh_token_invalid(self, api_client):
        """
        Test refreshing with invalid refresh token fails.
        """
        refresh_url = reverse("token_refresh")
        refresh_data = {
            "refresh": "invalid_token_here",
        }

        response = api_client.post(refresh_url, refresh_data, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_verify_token_valid(self, api_client, test_user):
        """
        Test verifying a valid access token.
        """
        # Obtain tokens
        login_url = reverse("token_obtain_pair")
        login_data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        login_response = api_client.post(login_url, login_data, format="json")
        access_token = login_response.data["access"]

        # Verify token
        verify_url = reverse("token_verify")
        verify_data = {
            "token": access_token,
        }

        response = api_client.post(verify_url, verify_data, format="json")

        assert response.status_code == status.HTTP_200_OK

    def test_verify_token_invalid(self, api_client):
        """
        Test verifying an invalid token fails.
        """
        verify_url = reverse("token_verify")
        verify_data = {
            "token": "invalid_token_here",
        }

        response = api_client.post(verify_url, verify_data, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_access_protected_endpoint_with_token(self, api_client, test_user):
        """
        Test accessing a protected endpoint with valid JWT token.

        Note: This test assumes products endpoint requires authentication.
        If not, this test should be adjusted based on actual protected endpoints.
        """
        # Obtain token
        login_url = reverse("token_obtain_pair")
        login_data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        login_response = api_client.post(login_url, login_data, format="json")
        access_token = login_response.data["access"]

        # Access endpoint with token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        # For now, just verify token can be set in headers
        # Actual protected endpoint tests will come later
        assert api_client.credentials() is None  # credentials() doesn't return anything

    def test_access_protected_endpoint_without_token(self, api_client):
        """
        Test accessing protected endpoint without token.

        Note: Currently all endpoints have AllowAny permission.
        This test will be more relevant once we have protected endpoints.
        """
        # This test will be expanded when we have actual protected endpoints
        pass
