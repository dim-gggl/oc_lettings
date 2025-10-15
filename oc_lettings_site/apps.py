"""Django application configuration."""

from django.apps import AppConfig
from django.apps import apps as django_apps


class OCLettingsSiteConfig(AppConfig):
    """
    Application configuration exposed via INSTALLED_APPS.
    Adjust pluralization for model verbose names.

    Methods:
        ready: Globally adjust pluralization for model verbose names.
    """
    name = 'oc_lettings_site'

    def ready(self):
        """
        Globally adjust pluralization for model verbose names:
        - If Django would naively pluralize as '<name>s' (or no plural set),
          and the base ends with: s, x, z, ch, sh -> use 'es'.
        - Special-case for '-z' to produce '<name>zes' (e.g., 'quiz' -> 'quizzes').
        """
        es_endings = ('s', 'x', 'ch', 'sh')  # endings that take 'es'
        for model in django_apps.get_models():
            opts = model._meta
            base = str(opts.verbose_name) if opts.verbose_name else ''
            if not base:
                continue
            plural = opts.verbose_name_plural

            # Only override if not explicitly set and Django's naive plural would be '<base>s'
            if plural is None or str(plural) == f"{base}s":
                if base.endswith('z'):
                    opts.verbose_name_plural = f"{base}zes"
                elif base.endswith(es_endings):
                    opts.verbose_name_plural = f"{base}es"
