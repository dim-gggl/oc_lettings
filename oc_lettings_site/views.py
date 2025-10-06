"""Home page view."""

from django.shortcuts import render


def index(request):
    """Render the landing page.

    Args:
    request : HttpRequest
        The incoming HTTP request.

    Returns:
    HttpResponse
        A rendered response for the 'index.html' template.
    """
    return render(request, 'index.html')
