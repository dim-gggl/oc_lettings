Orange County Lettings - CI/CD
==============================

This page documents the CI/CD workflow: local helpers (Makefile), GitHub Actions pipeline, and deployment to Render.

Makefile
--------

Targets overview:

- ``build``: build local Docker image (``IMAGE_NAME``/``TAG``)
- ``run-dev`` / ``run-prod``: run the image mapping port 8000 and binding the SQLite DB file
- ``pull-run``: pull from Docker Hub then run locally
- ``test``: run tests with coverage (outside Docker)
- ``push``: build and push multi-arch image to Docker Hub (``linux/amd64`` and ``linux/arm64``)
- ``clean``: remove local image

Key variables:

- ``IMAGE_NAME``: ``dgggl88/oc_lettings``
- ``TAG``: ``latest``
- ``ENV_FILE``: ``.env`` (source for ``DJANGO_SECRET_KEY`` in run targets)
- ``DB_FILE``: ``oc-lettings-site.sqlite3`` (bind-mounted into the container)

GitHub Actions
--------------

Workflow file: ``.github/workflows/ci.yml``

Jobs:

1) Lint
   - Setup Python 3.13
   - Install ``requirements.txt``
   - Run ``flake8``

2) Tests
   - Needs: Lint
   - Setup Python 3.13
   - Install dependencies
   - Run coverage with threshold (``--fail-under=80``)

3) Build and push Docker image (multi-arch)
   - Needs: Tests
   - Only on ``main``
   - Login to Docker Hub
   - Build and push tags: ``latest`` and ``<sha>`` for platforms ``linux/amd64, linux/arm64``

4) Deploy to Render
   - Needs: Build and push
   - Only on ``main``
   - Uses ``JorgeLNJunior/render-deploy`` with ``RENDER_SERVICE_ID`` and ``RENDER_API_KEY``

Read the Docs documentation deployment
--------------------------------------

The documentation is built with Sphinx and deployed on Read the Docs. Builds are
triggered automatically on every push via a GitHub → Read the Docs webhook.

Project configuration
~~~~~~~~~~~~~~~~~~~~~

- The Read the Docs config lives at the repository root: ``.readthedocs.yaml``.
  Minimal excerpt:

  .. code-block:: yaml

     version: 2
     build:
       os: ubuntu-22.04
       tools:
         python: "3.12"
     sphinx:
       configuration: docs/conf.py
       fail_on_warning: true
     python:
       install:
         - requirements: docs/requirements.txt

- Sphinx configuration: ``docs/conf.py``
- Documentation dependencies: ``docs/requirements.txt``

GitHub ↔ Read the Docs integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable automatic builds on push:

1. On Read the Docs (project Admin):
   - Go to ``Admin`` → ``Integrations`` → ``Add integration``.
   - Choose ``GitHub incoming webhook`` and copy the generated ``Payload URL``.

2. On GitHub (repository Settings):
   - ``Settings`` → ``Webhooks`` → ``Add webhook``.
   - Paste the ``Payload URL`` from Read the Docs.
   - Content type: ``application/json``.
   - Events: select ``Just the push event``.
   - Save the webhook.

3. Push to any branch. Read the Docs should receive the event and schedule a build
   using ``.readthedocs.yaml`` and ``docs/conf.py``.

Troubleshooting
~~~~~~~~~~~~~~~

- Ensure ``docs`` builds locally: ``sphinx-build -b html docs docs/_build/html``.
- Check that the webhook deliveries in GitHub show ``200`` responses.
- In Read the Docs, verify build logs and that the environment matches the YAML
  (Ubuntu 22.04, Python 3.12) and that dependencies from ``docs/requirements.txt``
  are installed.

Required secrets:

- ``DJANGO_SECRET_KEY`` (tests)
- ``DOCKER_USERNAME``, ``DOCKERHUB_TOKEN`` (Docker Hub)
- ``RENDER_SERVICE_ID``, ``RENDER_API_KEY`` (Render)

Generate secrets with Clinkey (recommended)
-------------------------------------------

- Web UI: see :doc:`clinkey`
- CLI example to generate a strong secret for GitHub Actions or Render:

  .. code-block:: bash

     pip install clinkey-cli
     clinkey -t super_strong -l 64 -s - --lower

Render deployment
-----------------

- Production URL: ``https://oc-lettings-x670.onrender.com``
- Render fetches the Docker image produced by CI and redeploys the service.
- Environment variables to set in Render:

  - ``ENV_MODE=prod``
  - ``DJANGO_SECRET_KEY`` (strong secret)
  - ``SENTRY_DSN`` (optional)

Local quick commands
--------------------

.. code-block:: bash

   # Build and run in dev
   make run-dev

   # Run tests with coverage
   make test

   # Push image to Docker Hub
   make push
