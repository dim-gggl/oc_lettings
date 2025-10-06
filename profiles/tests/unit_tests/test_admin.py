import pytest

from django.contrib import admin

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_is_registered_in_admin_site():
    assert Profile in admin.site._registry


