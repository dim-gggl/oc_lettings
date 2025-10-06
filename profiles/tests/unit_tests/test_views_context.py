import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index_context_contains_profiles_list(client, make_profile):
    make_profile(username="amy", favorite_city="Paris")
    make_profile(username="ben", favorite_city="Lyon")

    response = client.get(reverse("profiles_index"))

    profiles_list = response.context["profiles_list"]
    usernames = {p.user.username for p in profiles_list}

    assert len(profiles_list) == 2
    assert {"amy", "ben"}.issubset(usernames)


@pytest.mark.django_db
def test_profile_context_contains_profile(client, make_profile):
    profile = make_profile(username="iris", favorite_city="Berlin")

    response = client.get(reverse("profile", args=["iris"]))

    ctx_profile = response.context["profile"]
    assert ctx_profile.pk == profile.pk
    assert ctx_profile.user.username == "iris"
    assert ctx_profile.favorite_city == "Berlin"


