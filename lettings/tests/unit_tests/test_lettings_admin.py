import pytest

from django.contrib import admin

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_and_letting_registered_in_admin():
    """
    Test that the Address and Letting models are registered in the admin site.
    """
    assert Address in admin.site._registry
    assert Letting in admin.site._registry
