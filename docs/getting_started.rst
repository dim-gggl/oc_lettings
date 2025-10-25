Orange County Lettings - Getting Started
============================================================

This page explains how to set up the project locally: cloning, virtual environment, installation and dependencies.

Prerequisites
-------------

- Git CLI
- Python 3.13 (recommended)
- SQLite3 CLI
- Access to this repository

Clone the repository
--------------------

.. code-block:: bash

   git clone <your-fork-or-repo-url>
   cd oc_lettings

Create and activate a virtual environment
-----------------------------------------

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # On Windows PowerShell
   # .\\venv\\Scripts\\Activate.ps1

.. note::
   Always ensure the virtual environment is active before running commands.

Confirm environment is active
-----------------------------

.. code-block:: bash

   which python
   python --version
   which pip

Install dependencies
--------------------

The project uses a lockfile. Prefer installing from ``uv.lock`` when using ``uv``; otherwise use ``requirements.txt``.

- Using uv (recommended):

  .. code-block:: bash

     pip install uv
     uv sync

- Using pip:

  .. code-block:: bash

     pip install --requirement requirements.txt

Environment configuration
-------------------------

Copy and adjust a ``.env`` file if needed (see variables used in ``oc_lettings_site/settings.py``). A starter template is available as ``.env.example`` at the repo root.

- ``ENV_MODE``: dev or prod
- ``DJANGO_SECRET_KEY``: secret key for production
- ``SENTRY_DSN``: optional Sentry DSN

Generate strong secrets with Clinkey (optional)
-----------------------------------------------

- Web UI: see :doc:`clinkey`
- CLI example to export a strong Django secret key:

  .. code-block:: bash

     pip install clinkey-cli
     DJANGO_SECRET_KEY=$(clinkey -t super_strong -l 64 -s - --lower)

Run database migrations
-----------------------

.. code-block:: bash

   python manage.py migrate

Run the development server
--------------------------

.. code-block:: bash

   python manage.py runserver

Open ``http://localhost:8000`` in your browser.

Static files
------------

Static assets are served from ``static/`` in development. In production, files are collected to ``staticfiles/`` and served by WhiteNoise.

Common issues
-------------

- If the ``venv`` module is missing on Linux: ``sudo apt-get install python3-venv``
- Ensure the virtual environment is activated before running commands.
