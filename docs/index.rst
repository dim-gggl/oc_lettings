Orange County Lettings
======================

Purpose-built Django application for listing rentals and browsing user profiles.
This documentation guides external contributors and operators through setup,
development, testing, and deployment.

Overview
--------

- Project type: Django 5 application
- Apps: ``lettings``, ``profiles``
- Persistent store: SQLite (development), file-based via Docker bind mount (local runs)
- Static files: served by WhiteNoise in production

Audience
--------

- Developers integrating or contributing to the codebase
- Operators deploying and running the service

Quick start
-----------

Start with :doc:`start_here`, then follow :doc:`getting_started` for local setup.
For day-to-day commands and workflows, see :doc:`development`.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Topics

   start_here
   development
   deployment_ops
   reference
   README

