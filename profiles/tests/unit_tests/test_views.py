import pytest

from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from profiles.models import Profile
from profiles.views import index, profile as profile_view


class TestViews(TestCase):
    """Test views for the profiles application."""

    def test_profiles_index_status_code_200(self):
        """Profiles index responds with HTTP 200."""
        response = self.client.get(reverse("profiles"))
        self.assertEqual(response.status_code, 200)

    def test_profiles_index_template_used(self):
        """Profiles index uses the correct template."""
        response = self.client.get(reverse("profiles"))
        self.assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_profiles_index_displays_profiles_list(self):
        """Profiles index renders the list with links to each profile."""
        user1 = User.objects.create(username="jane")
        user2 = User.objects.create(username="john")
        Profile.objects.create(user=user1, favorite_city="Paris")
        Profile.objects.create(user=user2, favorite_city="Lyon")

        response = self.client.get(reverse("profiles"))

        self.assertContains(
            response,
            "<ul class=\"list-group list-group-flush list-group-careers\">",
            html=False
        )
        self.assertContains(
            response,
            "<li class=\"list-group-item\">",
            html=False
        )
        self.assertContains(response, "jane")
        self.assertContains(response, "john")
        self.assertContains(response, reverse("profile", args=["jane"]))
        self.assertContains(response, reverse("profile", args=["john"]))
        self.assertContains(response, "</ul>", html=False)

    def test_profiles_index_empty_state_message(self):
        """Profiles index shows an empty state when no profiles exist."""
        response = self.client.get(reverse("profiles"))
        self.assertContains(response, "No profiles are available.")

    @pytest.mark.django_db
    def test_profile_view_status_template_and_content(self):
        """Profile view renders expected fields for a given user."""
        user = User.objects.create(
            username="john_doe",
            first_name="John",
            last_name="Doe",
            email="john_doe@example.com",
        )
        Profile.objects.create(user=user, favorite_city="Berlin")

        response = self.client.get(reverse("profile", args=[user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, "john_doe")
        self.assertContains(response, "John")
        self.assertContains(response, "Doe")
        self.assertContains(response, "john_doe@example.com")
        self.assertContains(response, "Berlin")

    def test_reverse_and_resolve_profiles_index(self):
        """
        Reverse/resolve for profiles points to the correct view
        function.
        """
        url = reverse("profiles")
        resolved = resolve(url)
        self.assertEqual(resolved.func, index)

    def test_reverse_and_resolve_profile(self):
        """Reverse/resolve for profile points to the correct view function."""
        url = reverse("profile", args=["john"])
        resolved = resolve(url)
        self.assertEqual(resolved.func, profile_view)
