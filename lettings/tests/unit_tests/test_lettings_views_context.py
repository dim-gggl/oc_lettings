import pytest

from django.urls import reverse

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_context_contains_lettings_list(client):
    """Test that the lettings index context contains the lettings list."""
    addr1 = Address.objects.create(number=1,
                                   street="rue A",
                                   city="Cannes",
                                   state="FR",
                                   zip_code=83800,
                                   country_iso_code="FRA")
    addr2 = Address.objects.create(number=2,
                                   street="rue B",
                                   city="Dijon",
                                   state="FR",
                                   zip_code=21000,
                                   country_iso_code="FRA")
    Letting.objects.create(title="Letting 1", address=addr1)
    Letting.objects.create(title="Letting 2", address=addr2)

    response = client.get(reverse("lettings"))

    lettings_list = response.context["lettings_list"]
    assert len(lettings_list) == 2
    assert str(lettings_list[0]) == "Letting 1"
    assert str(lettings_list[1]) == "Letting 2"


@pytest.mark.django_db
def test_letting_context_contains_title_and_address(client):
    """Test that the letting context contains the title and address."""
    addr = Address.objects.create(number=10,
                                  street="rue parisienne",
                                  city="Paris",
                                  state="FR",
                                  zip_code=75001,
                                  country_iso_code="FRA")
    lett = Letting.objects.create(title="Super House", address=addr)

    response = client.get(reverse("letting", args=[lett.id]))

    assert response.context["title"] == "Super House"
    assert response.context["address"].pk == addr.pk
