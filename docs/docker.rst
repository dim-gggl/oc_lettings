Orange County Lettings - Docker
============================================================

This page explains how to use the published Docker image and how to build locally.

Pull the image
--------------

The image is available on Docker Hub:

.. code-block:: bash

   docker pull dgggl88/oc_lettings:latest

Run the container
-----------------

.. code-block:: bash

   docker run --rm -p 8000:8000 \
     -e ENV_MODE=prod \
     -e DJANGO_SECRET_KEY="your_super_strong_secret_key" \
     -e SENTRY_DSN="" \
     --name oc_lettings dgggl88/oc_lettings:latest

Then open ``http://localhost:8000``.

Notes:

- The image runs ``entrypoint.sh`` which applies migrations then starts Gunicorn on port 8000.
- Static files are collected at build time and served by WhiteNoise.

Environment variables
---------------------

- ``ENV_MODE``: ``dev`` or ``prod`` (controls debug and allowed hosts)
- ``DJANGO_SECRET_KEY``: required in production
- ``SENTRY_DSN``: optional, enable Sentry reporting

Generate DJANGO_SECRET_KEY with Clinkey (optional)
--------------------------------------------------

.. code-block:: bash

   pip install clinkey-cli
   DJANGO_SECRET_KEY=$(clinkey -t super_strong -l 64 -s - --lower)

Volume mounting (optional)
--------------------------

If you want to persist the SQLite database outside the container:

.. code-block:: bash

   docker run --rm -p 8000:8000 \
     -v $(pwd)/oc-lettings-site.sqlite3:/app/oc-lettings-site.sqlite3 \
     dgggl88/oc_lettings:latest

Build the image locally
-----------------------

.. code-block:: bash

   docker build -t oc_lettings:local .

Run the locally built image
---------------------------

.. code-block:: bash

   docker run --rm -p 8000:8000 oc_lettings:local

Compose example (optional)
--------------------------

.. code-block:: yaml

   services:
     web:
       image: dgggl88/oc_lettings:latest
       environment:
         ENV_MODE: prod
         DJANGO_SECRET_KEY: "change-me"
       ports:
         - "8000:8000"
