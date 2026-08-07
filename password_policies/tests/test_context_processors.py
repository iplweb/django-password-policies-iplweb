from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.test import TestCase

from password_policies.conf import settings
from password_policies.context_processors import password_status
from password_policies.models import PasswordHistory
from password_policies.tests.lib import create_user


class PasswordStatusContextProcessorTest(TestCase):
    def test_request_without_user_attribute(self):
        # A bare HttpRequest never went through AuthenticationMiddleware, so it
        # has no `user` at all. This happens while rendering the 500 page when
        # the original exception was raised before AuthenticationMiddleware ran,
        # and whenever a template is rendered outside the request/response cycle
        # (RequestFactory, e-mails, management commands, Celery tasks).
        # Blowing up here would mask the exception that is being handled.
        request = HttpRequest()
        self.assertFalse(hasattr(request, "user"))

        self.assertEqual({}, password_status(request))

    def test_request_with_user_set_to_none(self):
        # Django itself never does this, but third-party auth middleware and
        # test code do. Cf. https://github.com/iplweb/django-password-policies-iplweb/pull/21
        request = HttpRequest()
        request.user = None

        self.assertEqual({}, password_status(request))

    def test_anonymous_user(self):
        request = HttpRequest()
        request.user = AnonymousUser()

        self.assertEqual({}, password_status(request))

    def test_authenticated_user_change_not_required(self):
        request = HttpRequest()
        request.user = create_user()
        # a fresh history entry means the password has not expired yet;
        # `create_user` alone backdates `date_joined` past the expiry
        PasswordHistory.objects.create(user=request.user, password="testpass")
        request.session = {}

        self.assertEqual({"password_change_required": False}, password_status(request))

    def test_authenticated_user_change_required(self):
        request = HttpRequest()
        # `create_user` backdates `date_joined` past PASSWORD_DURATION_SECONDS
        # and creates no history, so the password counts as expired
        request.user = create_user()
        request.session = {}

        self.assertEqual({"password_change_required": True}, password_status(request))

    def test_authenticated_user_reads_cached_value_from_session(self):
        request = HttpRequest()
        request.user = create_user()
        request.session = {settings.PASSWORD_POLICIES_CHANGE_REQUIRED_SESSION_KEY: True}

        self.assertEqual({"password_change_required": True}, password_status(request))
