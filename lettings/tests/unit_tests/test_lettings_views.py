from django.urls import reverse, resolve
from django.test import TestCase

from lettings.models import Letting, Address
from lettings.views import index, letting as letting_view


class TestLettingsViews(TestCase):
    """Tests for lettings views."""

    def test_lettings_index_status_template_and_empty_state(self):
        """
        Test that the lettings index page is displayed and contains the
        correct content.
        """
        response = self.client.get(reverse("lettings"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "Lettings")
        self.assertContains(response, "No lettings are available.")

    def test_lettings_index_lists_lettings_and_links(self):
        """
        Test that the lettings index page lists the lettings and contains the
        correct links.
        """
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
        l1 = Letting.objects.create(title="Letting 1", address=addr1)
        l2 = Letting.objects.create(title="Letting 2", address=addr2)

        response = self.client.get(reverse("lettings"))
        self.assertContains(
            response,
            "<ul class=\"list-group list-group-flush list-group-careers\">",
            html=False
        )
        self.assertContains(response, "Letting 1")
        self.assertContains(response, "Letting 2")
        self.assertContains(response, reverse("letting", args=[l1.id]))
        self.assertContains(response, reverse("letting", args=[l2.id]))

    def test_letting_detail_status_template_and_content(self):
        """
        Test that the letting detail page is displayed and contains the
        correct content.
        """
        addr = Address.objects.create(number=10,
                                      street="rue parisienne",
                                      city="Paris",
                                      state="FR",
                                      zip_code=75001,
                                      country_iso_code="FRA")
        lett = Letting.objects.create(title="Super House", address=addr)

        response = self.client.get(reverse("letting", args=[lett.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, "Super House")
        self.assertContains(response, "10 rue parisienne")
        self.assertContains(response, "Paris, FR 75001")
        self.assertContains(response, "FRA")

    def test_reverse_and_resolve_lettings_index(self):
        """
        Test that the lettings index URL is resolved to the lettings index
        view.
        """
        url = reverse("lettings")
        resolved = resolve(url)
        self.assertEqual(resolved.func, index)

    def test_reverse_and_resolve_letting(self):
        """
        Test that the letting URL is resolved to the letting view.
        """
        url = reverse("letting", args=[1])
        resolved = resolve(url)
        self.assertEqual(resolved.func, letting_view)
