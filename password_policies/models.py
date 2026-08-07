from django.conf import settings as django_settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import signals
from django.utils import timezone
try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    # Before in Django 3.0
    from django.utils.translation import ugettext_lazy as _

from password_policies.conf import settings
from password_policies.managers import PasswordHistoryManager


class PasswordChangeRequired(models.Model):
    """
    Stores an entry to enforce password changes, related to :model:`auth.User`.

    Has the following fields:"""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        db_index=True,
        help_text=_("The date the entry was " "created."),
    )
    user = models.OneToOneField(
        django_settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        help_text=_("The user who needs to change " "his/her password."),
        related_name="password_change_required",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return _("Password change required for user %s") % self.user

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]
        verbose_name = _("enforced password change")
        verbose_name_plural = _("enforced password changes")


class PasswordHistory(models.Model):
    """
    Stores a single password history entry, related to :model:`auth.User`.

    Has the following fields:"""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        db_index=True,
        help_text=_("The date the entry was " "created."),
    )
    password = models.CharField(
        max_length=128,
        verbose_name=_("password"),
        help_text=_("The encrypted password."),
    )
    user = models.ForeignKey(
        django_settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        help_text=_("The user this password history " "entry belongs to."),
        related_name="password_history_entries",
        on_delete=models.CASCADE,
    )

    objects = PasswordHistoryManager()

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]
        verbose_name = _("password history entry")
        verbose_name_plural = _("password history entries")


class PasswordProfile(models.Model):
    """
    Stores a single password history entry, related to :model:`auth.User`.

    Has the following fields:"""

    created = models.DateTimeField(
        verbose_name=_("created"),
        db_index=True,
        help_text=_("The date the entry was " "created."),
        auto_now_add=True,
    )
    last_changed = models.DateTimeField(
        verbose_name=_("last changed"),
        db_index=True,
        help_text=_("The date the password was last changed."),
        auto_now=True,
    )
    user = models.OneToOneField(
        django_settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        help_text=_("The user this password profile " "belongs to."),
        related_name="password_profile",
        on_delete=models.CASCADE,
    )

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]
        verbose_name = _("password profile")
        verbose_name_plural = _("password profiles")


def create_password_profile_signal(sender, instance, created, **kwargs):
    if created:
        now = timezone.now()
        PasswordProfile.objects.create(user=instance, last_changed=now, created=now)


def password_change_signal(sender, instance, **kwargs):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=instance.pk)
        password1 = getattr(user, settings.PASSWORD_MODEL_FIELD)
        password2 = getattr(instance, settings.PASSWORD_MODEL_FIELD)
        if not password1 == password2:
            profile, _ign = PasswordProfile.objects.get_or_create(user=instance)
            profile.last_changed = timezone.now()
            profile.save()
    except user_model.DoesNotExist:
        pass


signals.pre_save.connect(
    password_change_signal,
    sender=django_settings.AUTH_USER_MODEL,
    dispatch_uid="password_change_signal",
)

signals.post_save.connect(
    create_password_profile_signal,
    sender=django_settings.AUTH_USER_MODEL,
    dispatch_uid="create_password_profile_signal",
)
