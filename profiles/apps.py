"""
Profiles application configuration.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Profiles application configuration exposed via INSTALLED_APPS.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
