"""
Views for the lettings application.

Functions:
    lettings_index: View to display the list of lettings.
    letting: View to display a letting's details.
"""

import logging
from django.shortcuts import render
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.db import DatabaseError
from django.http import Http404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    View to display the list of lettings.
    """
    try:
        lettings_list = Letting.objects.all()
    except DatabaseError as e:
        logger.error(f"Database error: {e}")
        raise

    context = {'lettings_list': lettings_list}
    try:
        return render(request, "lettings/index.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError):
        logger.error("Template error for lettings/index",
                     extra={"template": "lettings/index.html"},
                     exc_info=True)
        raise


def letting(request, letting_id):
    """Letting details with robust error logging."""
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning("Letting not found",
                       extra={"letting_id": letting_id, "path": request.path})
        raise Http404
    except Letting.MultipleObjectsReturned:
        logger.error("Multiple lettings returned",
                     extra={"letting_id": letting_id},
                     exc_info=True)
        raise
    except DatabaseError:
        logger.error("DB error while fetching letting",
                     extra={"letting_id": letting_id},
                     exc_info=True)
        raise

    context = {"title": letting.title, "address": letting.address}
    try:
        return render(request, "lettings/letting.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError):
        logger.error(
            "Template error for lettings/letting",
            extra={
                "template": "lettings/letting.html",
                "letting_id": letting_id
            },
            exc_info=True
        )
        raise
