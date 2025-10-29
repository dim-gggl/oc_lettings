<div align="center">

# Orange County Lettings

[![CI/CD](https://img.shields.io/github/actions/workflow/status/dim-gggl/oc_lettings/ci.yml?branch=main&label=CI%20%2F%20CD)](https://github.com/dim-gggl/oc_lettings/actions)
[![Docs](https://img.shields.io/readthedocs/oc-lettings?logo=readthedocs)](https://oc-lettingsdocs.readthedocs.io/latest/)
[![Last commit](https://img.shields.io/github/last-commit/dim-gggl/oc_lettings)](https://github.com/dim-gggl/oc_lettings/commits/main)
[![Docker pulls](https://img.shields.io/docker/pulls/dgggl88/oc_lettings?logo=docker)](https://hub.docker.com/r/dgggl88/oc_lettings)
[![Image size](https://img.shields.io/docker/image-size/dgggl88/oc_lettings/latest?logo=docker)](https://hub.docker.com/r/dgggl88/oc_lettings)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue?logo=python)](#)
[![Django 5.2](https://img.shields.io/badge/django-5.2-green?logo=django)](#)
[![Pytest](https://img.shields.io/badge/pytest-8.x-0A9EDC?logo=pytest)](#)
[![Coverage ≥80%](https://img.shields.io/badge/coverage-%3E%3D80%25-yellowgreen)](#)
[![Render](https://img.shields.io/badge/Render-Hosted-46E3B7?logo=render)](https://oc-lettings-670x.onrender.com)

</div>

## Overview

Orange County Lettings is a web application to browse lettings and user profiles. It is containerized with Docker, validated by automated CI, and deployed on Render. Full developer and operator documentation is published on Read the Docs.

- Production: [https://oc-lettings-670x.onrender.com](https://oc-lettings-670x.onrender.com)
- Docker image: [https://hub.docker.com/r/dgggl88/oc_lettings](https://hub.docker.com/r/dgggl88/oc_lettings)
- Documentation: [https://oc-lettingsdocs.readthedocs.io/latest/](https://oc-lettingsdocs.readthedocs.io/latest/)

## Tech stack

- Django 5.2, Python 3.13
- Pytest + Coverage, Flake8
- Docker, Docker Hub
- GitHub Actions CI/CD
- Render (deployment)
- Sphinx + Read the Docs (documentation)

## Documentation (condensed)

Below is a quick map of the documentation. Each item links to the corresponding full page on Read the Docs.

- Start here: get context, goals, and roles — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/start_here.html)
- Getting started: local setup and first run — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/getting_started.html)
- Development: day-to-day commands and workflows — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/development.html)
- Configuration: environment variables and settings — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/configuration.html)
- Models: domain models overview — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/models.html)
- Views: page views and endpoints — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/views.html)
- API: public interface and examples — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/api.html)
- Tests & coverage: running tests, thresholds, reports — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/tests_and_coverage.html)
- Deployment ops: secrets, environments, rollout — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/deployment_ops.html)
- Docker: images, run, and compose tips — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/docker.html)
- CI/CD: pipeline, jobs, artifacts — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/ci_cd.html)
- Error pages: 404/500 customization — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/error_pages.html)
- Sentry: monitoring and tracing — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/sentry.html)
- Architecture: modules and data flow — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/architecture.html)
- Reference: commands and quick lookup — [Full page](https://oc-lettingsdocs.readthedocs.io/latest/reference.html)

More at the docs index: https://oc-lettingsdocs.readthedocs.io/latest/

## Quickstart (local)

Prerequisites: Git, Python 3.13, SQLite3, Docker (optional).

1) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

2) Install dependencies and run the server

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://localhost:8000.

3) Lint, test, and coverage locally

```bash
flake8
pytest
coverage run -m pytest && coverage report
```

For the complete guide, see the [Development](https://oc-lettingsdocs.readthedocs.io/latest/development.html) and [Getting started](https://oc-lettingsdocs.readthedocs.io/latest/getting_started.html) pages.

## CI/CD and deployment

- GitHub Actions workflow: `.github/workflows/ci.yml` (lint → tests+coverage → Docker build/push → Render deploy)
- Docker Hub image: `dgggl88/oc_lettings`
- Render service: automatically redeployed on successful image push

See the full [CI/CD documentation](https://oc-lettingsdocs.readthedocs.io/latest/ci_cd.html) and [Deployment ops](https://oc-lettingsdocs.readthedocs.io/latest/deployment_ops.html).

