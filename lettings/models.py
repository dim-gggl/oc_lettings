"""
Lettings models.

Classes:
    Address: Address model to store the address of a letting.
    Letting: Letting model to store the letting of a property.
"""


from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Address model to store the address of a letting.

    Attributes:
        number: PositiveIntegerField to store the number of the address.
        street: CharField to store the street of the address.
        city: CharField to store the city of the address.
        state: CharField to store the state of the address.
        zip_code: PositiveIntegerField to store the zip code of the address.
        country_iso_code: CharField to store the country ISO code of the address.

    Methods:
        __str__: Returns the number and street of the address.
    """
    number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)]
    )
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2,
                            validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Letting model to store the letting of a property.

    Attributes:
        title: CharField to store the title of the letting.
        address: OneToOneField to the Address model.

    Methods:
        __str__: Returns the title of the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
