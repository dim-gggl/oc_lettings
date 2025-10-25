Orange County Lettings - Architecture
====================================================================

This page describes the high-level architecture of the project: Django apps, URL routing, modules and data flow.

Overview
--------

- Project package: ``oc_lettings_site``
- Applications: ``lettings``, ``profiles``
- Shared templates in ``templates/`` and app templates in each app
- Static assets under ``static/`` served by WhiteNoise
- SQLite database by default (see ``oc_lettings_site/settings.py``)

Applications
------------

oc_lettings_site
~~~~~~~~~~~~~~~~

- Purpose: site-level configuration, root URLs, WSGI/ASGI, index page and error handlers.
- URLs:

  .. code-block:: text

     /
     /sentry-debug/

- Key modules:

  - ``oc_lettings_site/urls.py``: includes app URLs and handlers
  - ``oc_lettings_site/views.py``: ``index``, ``custom_404``, ``custom_500``, ``sentry_debug``
  - ``oc_lettings_site/apps.py``: app config and pluralization tweaks

lettings
~~~~~~~~

- Purpose: manage lettings (list and detail display)
- URLs (mounted under ``/lettings/``):

  .. code-block:: text

     /lettings/
     /lettings/<letting_id>/

- Key modules:

  - ``lettings/urls.py``: URL patterns
  - ``lettings/views.py``: views for index and detail
  - ``lettings/models.py``: models including ``Letting`` and related address

profiles
~~~~~~~~

- Purpose: manage user profiles
- URLs (mounted under ``/profiles/``):

  .. code-block:: text

     /profiles/
     /profiles/<username>/

- Key modules:

  - ``profiles/urls.py``: URL patterns
  - ``profiles/views.py``: views for index and profile detail
  - ``profiles/models.py``: ``Profile`` model

URL routing
-----------

Root URL configuration includes app URLs and admin:

.. code-block:: python

   from django.contrib import admin
   from django.urls import path, include
   from oc_lettings_site import views

   urlpatterns = [
       path("", views.index, name="index"),
       path("lettings/", include("lettings.urls")),
       path("profiles/", include("profiles.urls")),
       path("admin/", admin.site.urls),
       path("sentry-debug/", views.sentry_debug, name="sentry-debug"),
   ]

Custom error handlers (active when ``DEBUG=False``):

- ``handler404 = "oc_lettings_site.views.custom_404"``
- ``handler500 = "oc_lettings_site.views.custom_500"``

Settings highlights
-------------------

- ``ENV_MODE`` controls ``DEBUG`` and ``ALLOWED_HOSTS``
- Static files: ``STATIC_URL``, ``STATICFILES_DIRS``, ``STATIC_ROOT``
- Logging configured with console handlers
- Sentry optional via ``SENTRY_DSN``

Data model (brief)
------------------

- ``profiles.Profile``: user profile with ``favorite_city``
- ``lettings.Address`` and ``lettings.Letting``: address normalized and linked to letting

Templates and static
--------------------

- Base templates in ``templates/``: ``index.html``, ``404.html``, ``500.html``, ``base.html``
- App templates in ``lettings/templates/lettings/`` and ``profiles/templates/profiles/``
- Static assets in ``static/`` (CSS, JS, fonts, images)
