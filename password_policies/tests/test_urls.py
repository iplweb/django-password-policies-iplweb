from django.test import TestCase
from django.urls import resolve, reverse

from password_policies.views import (
    PasswordChangeDoneView,
    PasswordChangeFormView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetFormView,
)


class URLPatternTestCase(TestCase):
    """Pins the published URLs of the app.

    The rest of the test suite reaches its views through ``reverse()``, which
    would happily follow a route that silently changed shape. These tests spell
    the paths out, so that a rewrite of ``urls.py`` cannot quietly break a
    project that has these URLs in its templates or in a user's bookmarks.
    """

    # ``password_policies.urls`` is included under "password/" by
    # password_policies.tests.urls.
    def test_static_routes_keep_their_paths(self):
        expected = {
            "password_change": "/password/change/",
            "password_change_done": "/password/change/done/",
            "password_reset": "/password/reset/",
            "password_reset_complete": "/password/reset/complete/",
            "password_reset_done": "/password/reset/done/",
        }
        self.assertEqual({name: reverse(name) for name in expected}, expected)

    def test_confirm_route_keeps_its_path(self):
        url = reverse("password_reset_confirm", args=("MQ", "abc123", "sig-value_1"))
        self.assertEqual(url, "/password/reset/confirm/MQ/abc123/sig-value_1/")

    def test_routes_resolve_to_their_views(self):
        expected = {
            "/password/change/": PasswordChangeFormView,
            "/password/change/done/": PasswordChangeDoneView,
            "/password/reset/": PasswordResetFormView,
            "/password/reset/complete/": PasswordResetCompleteView,
            "/password/reset/done/": PasswordResetDoneView,
            "/password/reset/confirm/MQ/abc123/sig-value_1/": PasswordResetConfirmView,
        }
        for path, view in expected.items():
            with self.subTest(path=path):
                self.assertIs(resolve(path).func.view_class, view)
