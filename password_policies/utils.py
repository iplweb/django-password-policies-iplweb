from datetime import timedelta, datetime

from django.utils import timezone
from django.conf import settings as django_settings
from django.core.exceptions import ObjectDoesNotExist

from password_policies.conf import settings
from password_policies.models import PasswordHistory


class PasswordCheck(object):
    "Checks if a given user needs to change his/her password."

    def __init__(self, user):
        self.user = user
        self.expiry_datetime = self.get_expiry_datetime()

    def is_required(self):
        """Checks if a given user is forced to change his/her password.

        If an instance of :class:`~password_policies.models.PasswordChangeRequired`
        exists the verification is successful.

        :returns: ``True`` if the user needs to change his/her password,
            ``False`` otherwise.
        :rtype: bool
        """
        try:
            if self.user.password_change_required:
                return True
        except ObjectDoesNotExist:
            pass
        return False

    def is_expired(self):
        """Checks if a given user's password has expired.

        :returns: ``True`` if the user's password has expired,
            ``False`` otherwise.
        :rtype: bool
        """
        if PasswordHistory.objects.change_required(self.user):
            return True
        return False

    def get_expiry_datetime(self):
        "Returns the date and time when the user's password has expired."
        seconds = settings.PASSWORD_DURATION_SECONDS
        return timezone.now() - timedelta(seconds=seconds)


def datetime_to_string(value, format=None):
    """Transform datetime object in a string with input format
    :returns: formatted datetime
    :rtype: str
    """
    if format is None:
        format = (
            "%Y-%m-%dT%H:%M:%S.%f%z"
            if django_settings.USE_TZ
            else "%Y-%m-%dT%H:%M:%S.%f"
        )

    if not isinstance(value, str):
        return datetime.strftime(value, format)
    else:
        return value


def string_to_datetime(value, format=None):
    """Transform string object in a datetime with input format
    :returns: formatted string
    :rtype: datetime
    """
    if format is None:
        format = (
            "%Y-%m-%dT%H:%M:%S.%f%z"
            if django_settings.USE_TZ
            else "%Y-%m-%dT%H:%M:%S.%f"
        )

    if not isinstance(value, datetime):
        return datetime.strptime(value, format)
    else:
        return value
