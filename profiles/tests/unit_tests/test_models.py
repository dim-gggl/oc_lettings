import pytest

from django.db import IntegrityError

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str_returns_username(django_user_model):
    """Test that the profile string representation returns the username."""
    user = django_user_model.objects.create_user(username="john_doe")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    assert str(profile) == "john_doe"


@pytest.mark.django_db
def test_profile_user_is_one_to_one(django_user_model):
    """Test that a profile can be created for a user."""
    user = django_user_model.objects.create_user(username="john_doe")
    Profile.objects.create(user=user)

    with pytest.raises(IntegrityError):
        Profile.objects.create(user=user)
