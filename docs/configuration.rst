Configuration
=============

This page explains environment configuration, the ``.env`` file, required variables, and the rationale behind keeping secrets stable.

How configuration is loaded
---------------------------

- ``python-dotenv`` loads variables from ``.env`` at startup (see ``load_dotenv()`` in ``oc_lettings_site/settings.py``)
- System environment variables take precedence over the ``.env`` file

Required environment variables
------------------------------

- ``ENV_MODE``
  - Values: ``dev`` (default), ``prod``
  - Controls: ``DEBUG`` flag and ``ALLOWED_HOSTS``

- ``DJANGO_SECRET_KEY``
  - Required in production
  - Used to sign sessions, CSRF tokens, and other cryptographic features
  - Keep it strong and stable across deployments to avoid invalidating sessions and tokens

- ``SENTRY_DSN`` (optional)
  - Enables Sentry error reporting

Using a .env file
-----------------

- Create a ``.env`` at the project root based on ``.env.example``
- Do not commit your ``.env`` file—store secrets securely

Example ``.env``:

.. code-block:: ini

   ENV_MODE=dev
   DJANGO_SECRET_KEY=your_super_strong_secret_key
   SENTRY_DSN=

Generating secrets
------------------

- See :doc:`clinkey` for web UI and CLI
- Example:

  .. code-block:: bash

     pip install clinkey-cli
     DJANGO_SECRET_KEY=$(clinkey -t super_strong -l 64 -s - --lower)

Secret key stability and data access
------------------------------------

- ``DJANGO_SECRET_KEY`` does not control direct database access
- Changing it invalidates signed data (sessions, password reset tokens, some caches)
- For production, plan rotations to minimize user impact (e.g., scheduled maintenance)

Deployment notes
----------------

- On Docker: set variables via ``-e`` or a compose file
- On Render: set variables in the service dashboard
- In CI: store secrets in GitHub Actions secrets (never in code)
