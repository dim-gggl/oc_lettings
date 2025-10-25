Orange County Lettings - Tests and Coverage
============================================================

This page explains how to run tests and measure coverage locally.

Test stack
----------

- ``pytest``: test runner
- ``pytest-django``: Django integration
- ``pytest-cov``: coverage reporting

Run unit tests
--------------

Always ensure your virtual environment is active before running commands.

.. code-block:: bash

   source venv/bin/activate
   pytest -q

Run tests with coverage
-----------------------

.. code-block:: bash

   pytest --cov=oc_lettings_site --cov=profiles --cov=lettings --cov-report=term-missing

Generate HTML coverage report
-----------------------------

.. code-block:: bash

   pytest --cov=oc_lettings_site --cov=profiles --cov=lettings --cov-report=html
   # Open HTML report
   open htmlcov/index.html  # macOS
   # xdg-open htmlcov/index.html  # Linux

Continuous integration tips
---------------------------

- Use ``--maxfail=1 -q`` locally to fail fast.
- Keep coverage thresholds consistent across environments if you enforce minimums.

Troubleshooting
---------------

- Make sure ``DJANGO_SETTINGS_MODULE`` is correctly set (see ``pytest.ini``).
- If database errors occur, run ``python manage.py migrate`` before tests.
- If the environment variable ``ENV_MODE`` influences behavior, set it to ``dev`` for local tests.
