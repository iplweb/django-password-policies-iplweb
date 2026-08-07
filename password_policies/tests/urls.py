from django.urls import include, path

from password_policies.tests.views import TestHomeView, TestLoggedOutMixinView

urlpatterns = [
    path("password/", include("password_policies.urls")),
    path("", TestHomeView.as_view(), name="home"),
    path("fubar/", TestLoggedOutMixinView.as_view(), name="loggedoutmixin"),
]
