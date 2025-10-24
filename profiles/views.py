"""
Views for the profiles application.

Functions:
    profiles_index: View to display the list of profiles.
    profile: View to display a profile's details.
"""

from django.shortcuts import render
from django.db import DatabaseError
from django.http import Http404
from django.template import TemplateSyntaxError, TemplateDoesNotExist
import logging
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    View to display the list of profiles.
    """
    try:
        profiles_list = Profile.objects.all()
    except DatabaseError:
        logger.error("DB error while listing profiles",
                     extra={"path": request.path},
                     exc_info=True)
        raise

    context = {"profiles_list": profiles_list}
    try:
        return render(request, "profiles/index.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError):
        logger.error("Template error for profiles/index",
                     extra={"template": "profiles/index.html"},
                     exc_info=True)
        raise


def profile(request, username):
    """
    View to display a profile's details.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning("Profile not found",
                       extra={
                        "username": username,
                        "path": request.path
                       },
                       exc_info=True)
        raise Http404("Profile not found")
    except DatabaseError:
        logger.error("Database error while fetching profile",
                     extra={"username": username},
                     exc_info=True)
        raise

    context = {"profile": profile}
    try:
        return render(request, "profiles/profile.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError):
        logger.error("Template error for profiles/profile",
                     extra={
                        "template": "profiles/profile.html",
                        "username": username
                     },
                     exc_info=True)
        raise
