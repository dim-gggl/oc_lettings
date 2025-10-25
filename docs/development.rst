Development
===========

Guides for local development, testing, tooling, and documentation.

Run the application
-------------------

.. code-block:: bash

   python manage.py runserver

Run tests and coverage
----------------------

.. code-block:: bash

   coverage run -m pytest
   coverage report -m

Linting and code style
----------------------

.. code-block:: bash

   flake8

Database and migrations
-----------------------

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

Static files
------------

Static assets are served from ``static/`` in development. In production, files
are collected to ``staticfiles/`` and served by WhiteNoise.

Build and view documentation (Sphinx)
-------------------------------------

.. code-block:: bash

   # From the repository root
   pip install -r docs/requirements.txt
   sphinx-build -b html docs docs/_build/html
   # Then open docs/_build/html/index.html in your browser

Additional guides
-----------------

.. toctree::
   :maxdepth: 2

   tests_and_coverage
   clinkey
