from password_policies.conf import settings
from password_policies.models import PasswordHistory


def password_status(request):
    """
Adds a variable determining the state of a user's password
to the context if the user has authenticated:

* ``password_change_required``
    Determines if the user needs to change his/her password.

    Set to ``True`` if the user has to change his/her password,
    ``False`` otherwise.

To use it add it to the list of ``TEMPLATE_CONTEXT_PROCESSORS``
in a project's settings file::

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.contrib.messages.context_processors.messages',
        'password_policies.context_processors.password_status',
    )
"""
    d = {}
    # `request.user` only exists once AuthenticationMiddleware has run. It is
    # missing while Django renders the 500 page for an exception raised earlier
    # in the middleware chain, and whenever a template is rendered outside the
    # request/response cycle (RequestFactory, e-mails, management commands).
    # Raising here would mask the exception actually being handled, so bail out
    # quietly instead -- exactly what Django does in its own auth context
    # processor. `None` is not something Django produces, but third-party auth
    # middleware does; see https://github.com/iplweb/django-password-policies-iplweb/pull/21
    user = getattr(request, "user", None)
    if user is not None and user.is_authenticated:
        if settings.PASSWORD_POLICIES_CHANGE_REQUIRED_SESSION_KEY not in request.session:
            r = PasswordHistory.objects.change_required(request.user)
        else:
            r = request.session[settings.PASSWORD_POLICIES_CHANGE_REQUIRED_SESSION_KEY]
        d['password_change_required'] = r
    return d
