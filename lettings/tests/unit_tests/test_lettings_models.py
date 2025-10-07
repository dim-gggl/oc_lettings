import pytest

from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_address_str_returns_number_and_street(make_address):
    """
    Test that the address string representation returns the number and street.
    """
    address = make_address(number=42, street="rue de Python")
    assert str(address) == "42 rue de Python"


@pytest.mark.django_db
def test_address_field_validators_enforced(make_address):
    """Test that the address field validators are enforced."""
    address = make_address(
        number=100000,  # invalid (> 9999)
        street="S",
        city="",
        state="F",  # too short
        zip_code=100000,  # invalid (> 99999)
        country_iso_code="FR",  # too short
    )
    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_letting_str_returns_title(make_letting):
    """Test that the letting string representation returns the title."""
    letting = make_letting(title="Super House")
    assert str(letting) == "Super House"
