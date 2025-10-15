"""Home page and error handlers views."""

from django.shortcuts import render


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
    return render(request, "500.html", status=500)
