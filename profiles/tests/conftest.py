import pytest

from profiles.models import Profile


@pytest.fixture
def make_user(django_user_model):
    """Factory to create a Django user with sensible defaults."""
    def _make_user(username="user_test", password="password123", **kwargs):
        defaults = {
            "username": username,
            "password": password,
            "first_name": kwargs.pop("first_name", ""),
            "last_name": kwargs.pop("last_name", ""),
            "email": kwargs.pop("email", ""),
        }
        defaults.update(kwargs)
        return django_user_model.objects.create_user(**defaults)

    return _make_user


@pytest.fixture
def make_profile(make_user):
    """Factory to create a Profile for a given username and favorite city."""
    def _make_profile(username="user_test", favorite_city="Paris"):
        user = make_user(username=username)
        return Profile.objects.create(user=user, favorite_city=favorite_city)

    return _make_profile
