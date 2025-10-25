"""Home page and error handlers views."""

import logging
import os

from django.shortcuts import render
from sentry_sdk import capture_message


def index(request):
    """Render the landing page.

    Args:
    request : HttpRequest
        The incoming HTTP request.

    Returns:
    HttpResponse
        A rendered response for the "index.html" template.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    """Render custom 404 page.

    Args:
    request : HttpRequest
        The incoming HTTP request.
    exception : Exception
        The exception that triggered the 404 handler.

    Returns:
    HttpResponse
        A rendered response for the "404.html" template with 404 status.
    """
    logger = logging.getLogger("django.request")
    # Log 404 with path and referrer for diagnosis
    logger.warning(
        "404 Not Found: path=%s, referer=%s",
        request.get_full_path(),
        request.META.get("HTTP_REFERER"),
    )

    # Send a Sentry message (not an exception) only in production
    if os.environ.get("ENV_MODE") == "prod":
        capture_message(
            f"404 Not Found at {request.get_full_path()}",
            level="warning",
        )

    return render(request, "404.html", status=404)


def custom_500(request):
    """Render custom 500 page.

    Args:
    request : HttpRequest
        The incoming HTTP request.

    Returns:
    HttpResponse
        A rendered response for the "500.html" template with 500 status.
    """
    logger = logging.getLogger("django.request")
    # 500 handler is called after an exception; Django/Sentry already captured it.
    # We add a concise log for correlation without re-raising.
    logger.error("500 Internal Server Error at %s", request.get_full_path())
    return render(request, "500.html", status=500)


def sentry_debug(request):
    """Trigger a Sentry error for debugging."""
    1 / 0
