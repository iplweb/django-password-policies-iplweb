from django.urls import path, re_path

from password_policies.views import (
    PasswordChangeDoneView,
    PasswordChangeFormView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetFormView,
)

urlpatterns = [
    path("change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("change/", PasswordChangeFormView.as_view(), name="password_change"),
    path("reset/", PasswordResetFormView.as_view(), name="password_reset"),
    path(
        "reset/complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # Stays a regex route: the view takes the three components positionally and
    # constrains their length, which path() converters cannot express.
    re_path(
        r"^reset/confirm/([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13})/([0-9A-Za-z-=_]{1,128})/$",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
]
