import pytest

from lettings.models import Address, Letting


@pytest.fixture
def make_address():
    """Factory to create an Address instance with defaults."""
    def _make_address(
        number=1,
        street="rue de Rivoli",
        city="Paris",
        state="FR",
        zip_code=75001,
        country_iso_code="FRA",
    ):
        return Address.objects.create(
            number=number,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            country_iso_code=country_iso_code,
        )

    return _make_address


@pytest.fixture
def make_letting(make_address):
    """Factory to create a Letting instance linked to an Address."""
    def _make_letting(title="Super House", address=None):
        if not address:
            address = make_address()
        return Letting.objects.create(title=title, address=address)

    return _make_letting
