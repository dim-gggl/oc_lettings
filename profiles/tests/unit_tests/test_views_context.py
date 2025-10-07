import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index_context_contains_profiles_list(client, make_profile):
    """Test that the profiles index context contains the profiles list."""
    make_profile(username="jane", favorite_city="Paris")
    make_profile(username="john", favorite_city="Lyon")

    response = client.get(reverse("profiles_index"))

    profiles_list = response.context["profiles_list"]
    usernames = {p.user.username for p in profiles_list}

    assert len(profiles_list) == 2
    assert {"jane", "john"}.issubset(usernames)


@pytest.mark.django_db
def test_profile_context_contains_profile(client, make_profile):
    """Test that the profile context contains the profile."""
    profile = make_profile(username="john_doe", favorite_city="Berlin")

    response = client.get(reverse("profile", args=["john_doe"]))

    ctx_profile = response.context["profile"]
    assert ctx_profile.pk == profile.pk
    assert ctx_profile.user.username == "john_doe"
    assert ctx_profile.favorite_city == "Berlin"
