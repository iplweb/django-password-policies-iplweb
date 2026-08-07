from django.test import TestCase

from password_policies.conf import settings
from password_policies.models import (
    PasswordChangeRequired,
    PasswordHistory,
    PasswordProfile,
)
from password_policies.tests.lib import create_password_history, create_user, passwords


class PasswordHistoryModelTestCase(TestCase):
    def setUp(self):
        self.user = create_user()
        create_password_history(self.user)
        return super(PasswordHistoryModelTestCase, self).setUp()

    def test_password_history_expiration_with_offset(self):
        offset = settings.PASSWORD_HISTORY_COUNT + 2
        PasswordHistory.objects.delete_expired(self.user, offset=offset)
        count = PasswordHistory.objects.filter(user=self.user).count()
        self.assertEqual(count, offset)

    def test_password_history_expiration(self):
        PasswordHistory.objects.delete_expired(self.user)
        count = PasswordHistory.objects.filter(user=self.user).count()
        self.assertEqual(count, settings.PASSWORD_HISTORY_COUNT)

    def test_password_history_recent_passwords(self):
        self.assertFalse(PasswordHistory.objects.check_password(self.user, passwords[-1]))


class ModelStrTestCase(TestCase):
    """Every model must render as a useful string in the admin change lists."""

    def setUp(self):
        self.user = create_user()
        return super().setUp()

    def test_password_change_required_str_identifies_the_user(self):
        entry = PasswordChangeRequired.objects.create(user=self.user)
        self.assertIn("alice", str(entry))

    def test_password_history_str_identifies_the_user(self):
        entry = PasswordHistory.objects.create(user=self.user, password="x")
        self.assertIn("alice", str(entry))

    def test_password_profile_str_identifies_the_user(self):
        profile = PasswordProfile.objects.get(user=self.user)
        self.assertIn("alice", str(profile))
