import importlib
from django.core.signals import setting_changed
from django.dispatch import receiver
from .conf import settings as password_settings


@receiver(setting_changed)
def app_settings_reload_handler(**kwargs):
    """
    When you modify settings in your test using override_settings, we need to reload the app settings module
    this receiver is in fact imported in tests/__init__.py module
    """
    if "PASSWORD_" in kwargs["setting"]:
        importlib.reload(password_settings)
