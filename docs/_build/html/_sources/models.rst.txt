Orange County Lettings - Models
============================================================

This page documents the data models used by the project and explains the pluralization behavior.

Lettings app
------------

Address
~~~~~~~

- Fields:

  - ``number``: ``PositiveIntegerField`` (max 9999)
  - ``street``: ``CharField(64)``
  - ``city``: ``CharField(64)``
  - ``state``: ``CharField(2)`` with ``MinLengthValidator(2)``
  - ``zip_code``: ``PositiveIntegerField`` (max 99999)
  - ``country_iso_code``: ``CharField(3)`` with ``MinLengthValidator(3)``

- String representation: ``"<number> <street>"``

Letting
~~~~~~~

- Fields:

  - ``title``: ``CharField(256)``
  - ``address``: ``OneToOneField(Address, on_delete=CASCADE)``

- String representation: ``title``

Profiles app
------------

Profile
~~~~~~~

- Fields:

  - ``user``: ``OneToOneField(User, on_delete=CASCADE)``
  - ``favorite_city``: ``CharField(64, blank=True)``

- String representation: ``username``

Pluralization behavior (admin and elsewhere)
--------------------------------------------------------------------

Django normally derives plural forms from ``verbose_name`` automatically (often by appending ``s``). This project adjusts pluralization globally in ``oc_lettings_site/apps.py`` inside ``OCLettingsSiteConfig.ready`` to better handle English words ending with specific letters.

Rules applied at startup:

- If a model's plural name is not explicitly set and the naive plural would be ``<base>s`` then:
  - If ``base`` ends with ``z``: use ``<base>zes`` (e.g., ``quiz`` → ``quizzes``)
  - If ``base`` ends with ``s``, ``x``, ``ch``, or ``sh``: use ``<base>es``

This ensures that names like ``Address`` are pluralized as ``Addresses`` (displayed as "Addresses" in admin lists and related UI) without having to set ``verbose_name_plural`` on each model.

Refer to the implementation:

.. code-block:: python

   # oc_lettings_site/apps.py (excerpt)
   class OCLettingsSiteConfig(AppConfig):
       def ready(self):
           es_endings = ('s', 'x', 'ch', 'sh')
           for model in django_apps.get_models():
               opts = model._meta
               base = str(opts.verbose_name) if opts.verbose_name else ''
               if not base:
                   continue
               plural = opts.verbose_name_plural
               if plural is None or str(plural) == f"{base}s":
                   if base.endswith('z'):
                       opts.verbose_name_plural = f"{base}zes"
                   elif base.endswith(es_endings):
                       opts.verbose_name_plural = f"{base}es"

Note: You can still override plural forms per model by setting ``verbose_name`` and/or ``verbose_name_plural`` in a model's ``Meta`` class if needed.
