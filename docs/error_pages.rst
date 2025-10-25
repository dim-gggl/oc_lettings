Orange County Lettings - Error Pages
============================================================

This page documents the custom error pages and how they are handled.

Overview
--------

- Custom handlers are enabled when ``DEBUG=False``
- Configured in ``oc_lettings_site/urls.py``:

  - ``handler404 = "oc_lettings_site.views.custom_404"``
  - ``handler500 = "oc_lettings_site.views.custom_500"``

Handlers
--------

custom_404
~~~~~~~~~~

- Logs a warning with request path and referer
- Sends a non-exception message to Sentry in production (if ``SENTRY_DSN`` set)
- Renders ``templates/404.html`` with HTTP 404 status

custom_500
~~~~~~~~~~

- Logs an error with request path
- Renders ``templates/500.html`` with HTTP 500 status

Templates
---------

- Global templates are located under ``templates/``
- ``templates/404.html``: shown when a page is not found
- ``templates/500.html``: shown for server errors

Local testing tips
------------------

- To preview ``404.html`` locally: set ``DEBUG=False`` and request a missing route
- To trigger ``500.html`` locally: set ``DEBUG=False`` and visit ``/sentry-debug/`` (raises an error)
- Ensure environment variable ``ENV_MODE=prod`` if you want to mimic production behavior
