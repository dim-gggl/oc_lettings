"""
Profile model previously implemented in the oc_lettings_site application.

Classes:
    User: Default Django User model.
    Profile: Profile model based on the default Django User model.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model based on the default Django User model.

    Attributes:
        user: One-to-one field to the default Django User model.
        favorite_city: CharField to store the user's favorite city.

    Methods:
        __str__: Returns the username of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
