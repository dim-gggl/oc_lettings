Orange County Lettings - Sentry
============================================================

This page explains how Sentry is integrated in the project and how exceptions are captured both from explicit errors and error pages.

Overview
--------

- Sentry is optional and enabled when the environment variable ``SENTRY_DSN`` is set.
- Initialization occurs in ``oc_lettings_site/settings.py`` with ``sentry_sdk.init`` using ``DjangoIntegration`` and ``LoggingIntegration``.
- In production (``ENV_MODE=prod``), error handlers may send events to Sentry.

Initialization
--------------

- Environment variable: ``SENTRY_DSN`` must be set (e.g., in Render or your environment).
- Configuration highlights:

  - ``send_default_pii=True`` to include request context
  - ``traces_sample_rate=1.0`` for full transaction traces (tune in production)
  - ``LoggingIntegration`` captures logs (``event_level=ERROR``)
  - ``DjangoIntegration`` captures exceptions during requests and signals

Triggering an exception for testing
-----------------------------------

- Route ``/sentry-debug/`` deliberately raises an exception to validate Sentry capture.

404 and 500 pages
-----------------

- ``custom_404``: logs a warning and, when ``ENV_MODE=prod``, sends a message (``capture_message``) with level ``warning``
- ``custom_500``: returns the 500 template; uncaught exceptions have already been captured by Sentry/Django

Views and try/except
--------------------

- Views in ``lettings`` and ``profiles`` use ``try/except`` to:

  - Log database errors with ``exc_info=True``
  - Raise ``Http404`` for not found cases
  - Log template errors (``TemplateDoesNotExist``, ``TemplateSyntaxError``)

- These exceptions are either handled (404) or re-raised so that Sentry can capture them when applicable.

Local tips
----------

- Set ``ENV_MODE=prod`` and a valid ``SENTRY_DSN`` to mimic production behavior.
- Use ``/sentry-debug/`` to verify that Sentry receives events from the environment.
