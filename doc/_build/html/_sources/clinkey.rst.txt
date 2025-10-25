Orange County Lettings - Clinkey
========================================================

This page explains how to generate strong secrets and passwords using Clinkey.

Web interface
-------------

- Visit the Clinkey web UI: ``https://dim-gggl.github.io/Clinkey/``

Command-line interface
----------------------

Install via pip:

.. code-block:: bash

   pip install clinkey-cli

Or via Homebrew tap:

.. code-block:: bash

   brew tap dim-gggl/homebrew
   brew install clinkey

Examples
--------

Generate a strong Django secret key and export it as an environment variable:

.. code-block:: bash

   DJANGO_SECRET_KEY=$(clinkey -t super_strong -l 64 -s - --lower)

Tips
----

- For production, store the generated secret in a secure secret manager (e.g., GitHub Actions secrets, Render environment variables), not in source control.
- You can also generate other credentials (DB passwords, API keys) with appropriate templates and options.
