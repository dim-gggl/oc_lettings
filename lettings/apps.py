"""
Lettings application configuration.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Lettings application configuration exposed via INSTALLED_APPS.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
