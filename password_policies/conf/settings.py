from django.conf import settings
from django.contrib import auth

#: Determines which fields should be searched upon
#: in the admin change list of
#: the :class:`~password_policies.models.PasswordChangeRequired`
PASSWORD_CHANGE_REQUIRED_ADMIN_SEARCH_FIELDS = getattr(
    settings,
    "PASSWORD_CHANGE_REQUIRED_ADMIN_SEARCH_FIELDS",
    [
        "id",
        "user__id",
        "user__first_name",
        "user__email",
        "user__last_name",
        "user__username",
    ],
)


#: Determines wether the :middleware:`PasswordChangeMiddleware`
#: should ignore the logout views, allowing the user to log out
#: even if a password change is required.
PASSWORD_CHANGE_MIDDLEWARE_ALLOW_LOGOUT = getattr(
    settings, "PASSWORD_CHANGE_MIDDLEWARE_ALLOW_LOGOUT", True
)
#: A list of raw strings representing paths to ignore
#: while checking if a user has to change his/her password.
PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_PATHS = getattr(
    settings, "PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_PATHS", []
)
#: A list of usernames to exclude from password expiry checks
#: in the :middleware:`PasswordChangeMiddleware`.
#: Users in this list will never be forced to change their
#: password due to expiration.
#:
#: Useful for service accounts or bot users that should not
#: be subject to password rotation policies.
PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_USERNAMES = getattr(
    settings, "PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_USERNAMES", []
)
#: A list of usernames to exclude from password complexity
#: validation in :form:`PasswordPoliciesForm` and its subclasses.
#: Users in this list will not have their passwords checked
#: against complexity rules (character composition, entropy,
#: dictionary words, etc.) or password history.
#:
#: Useful for service accounts or bot users that manage
#: their own passwords programmatically.
PASSWORD_COMPLEXITY_EXCLUDED_USERNAMES = getattr(
    settings, "PASSWORD_COMPLEXITY_EXCLUDED_USERNAMES", []
)
#: Determines after how many seconds a check shall
#: be performed if the user's password has expired.
#:
#: Defaults to 1 hour.
PASSWORD_CHECK_SECONDS = getattr(settings, "PASSWORD_CHECK_SECONDS", 60 ** 2)

#: Specifies a list of common sequences to attempt to
#: match a password against.
PASSWORD_COMMON_SEQUENCES = getattr(
    settings,
    "PASSWORD_COMMON_SEQUENCES",
    [
        u"0123456789",
        u"`1234567890-=",
        u"~!@#$%^&*()_+",
        u"abcdefghijklmnopqrstuvwxyz",
        u"quertyuiop[]\\asdfghjkl;'zxcvbnm,./",
        u'quertyuiop{}|asdfghjkl;"zxcvbnm<>?',
        u"quertyuiopasdfghjklzxcvbnm",
        u"1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-['=]\\",
        u"qazwsxedcrfvtgbyhnujmikolp",
    ],
)
PASSWORD_DICTIONARY = getattr(settings, "PASSWORD_DICTIONARY", None)
"""
Specifies the location of a dictionary (file with one
word per line). Could be "/usr/share/dict/words".

Used by the :validator:`DictionaryValidator`.
"""
#: A minimum distance of the difference between old and
#: new password. A positive integer. Values greater
#: than 1 are recommended.
#:
#: A value of 0 disables
#: password similarity verification.
PASSWORD_DIFFERENCE_DISTANCE = getattr(settings, "PASSWORD_DIFFERENCE_DISTANCE", 3)
#: Don't log the person out in the middle of a session. Only do the checks at login time.
PASSWORD_CHECK_ONLY_AT_LOGIN = getattr(settings, "PASSWORD_CHECK_ONLY_AT_LOGIN", False)
#: Determines after how many seconds a user is forced
#: to change his/her password.
#:
#: Defaults to 60 days.
PASSWORD_DURATION_SECONDS = getattr(settings, "PASSWORD_DURATION_SECONDS", 24 * 60 ** 3)
#: The field on the user model as defined by settings.AUTH_USER_MODEL
#: where the password is stored.
PASSWORD_MODEL_FIELD = getattr(settings, "PASSWORD_MODEL_FIELD", "password")
#: Determines which fields should be searched upon
#: in the admin change list of
#: the :class:`~password_policies.models.PasswordHistory`
PASSWORD_HISTORY_ADMIN_SEARCH_FIELDS = getattr(
    settings,
    "PASSWORD_HISTORY_ADMIN_SEARCH_FIELDS",
    [
        "id",
        "user__id",
        "user__first_name",
        "user__email",
        "user__last_name",
        "user__username",
    ],
)
#: Specifies the number of user's previous passwords to
#: remember when the password history is being used.
#:
#: Defaults to 10 entries.
PASSWORD_HISTORY_COUNT = getattr(settings, "PASSWORD_HISTORY_COUNT", 10)
#: Specifies how close a fuzzy match has to be,
#: considered a match.
#:
#: Used by the :validator:`CommonSequenceValidator`.
PASSWORD_MATCH_THRESHOLD = getattr(settings, "PASSWORD_MATCH_THRESHOLD", 0.9)
#: Specifies the maximum amount of consecutive characters
#: allowed in passwords.
#:
#: Used by the :validator:`ConsecutiveCountValidator`.
PASSWORD_MAX_CONSECUTIVE = getattr(settings, "PASSWORD_MAX_CONSECUTIVE", 3)
#: Specifies the maximum length for passwords.
#:
#: Used by the :formfield:`PasswordPoliciesField`.
PASSWORD_MAX_LENGTH = getattr(settings, "PASSWORD_MAX_LENGTH", None)
#: Specifies the minimum entropy of long passwords
#: (len(password) >= 100).
#:
#: Used by the :validator:`EntropyValidator`.
PASSWORD_MIN_ENTROPY_LONG = getattr(settings, "PASSWORD_MIN_ENTROPY_LONG", 5.3)
#: Specifies the minimum entropy of short passwords
#: (len(password) < 100).
#:
#: Used by the :validator:`EntropyValidator`.
PASSWORD_MIN_ENTROPY_SHORT = getattr(settings, "PASSWORD_MIN_ENTROPY_SHORT", 0.8)
#: Specifies the minimum length for passwords.
#:
#: Used by the :formfield:`PasswordPoliciesField`.
PASSWORD_MIN_LENGTH = getattr(settings, "PASSWORD_MIN_LENGTH", 8)
#: Specifies the minimum amount of required letters in a
#: password.
#:
#: Used by :validator:`LetterCountValidator`.
PASSWORD_MIN_LETTERS = getattr(settings, "PASSWORD_MIN_LETTERS", 3)
#: Specifies the minimum amount of required lowercase letters in a
#: password.
#:
#: Used by :validator:`LowercaseLetterCountValidator`.
PASSWORD_MIN_LOWERCASE_LETTERS = getattr(settings, "PASSWORD_MIN_LOWERCASE_LETTERS", 0)
#: Specifies the minimum amount of required uppercase letters in a
#: password.
#:
#: Used by :validator:`UppercaseLetterCountValidator`.
PASSWORD_MIN_UPPERCASE_LETTERS = getattr(settings, "PASSWORD_MIN_UPPERCASE_LETTERS", 0)
#: Specifies the minimum amount of required numbers in a
#: password.
#:
#: Used by the :validator:`NumberCountValidator`.
PASSWORD_MIN_NUMBERS = getattr(settings, "PASSWORD_MIN_NUMBERS", 1)
#: Specifies the minimum amount of required symbols in a
#: password.
#:
#: Used by :validator:`SymbolCountValidator`.
PASSWORD_MIN_SYMBOLS = getattr(settings, "PASSWORD_MIN_SYMBOLS", 1)
#: Determines wether to validate passwords using the
#: :validator:`CracklibValidator`.
PASSWORD_USE_CRACKLIB = getattr(settings, "PASSWORD_USE_CRACKLIB", False)
#: Determines wether to use the password history.
PASSWORD_USE_HISTORY = getattr(settings, "PASSWORD_USE_HISTORY", True)
#: A list of project specific words to check a password
#: against.
#:
#: Used by the :validator:`DictionaryValidator`.
PASSWORD_WORDS = getattr(settings, "PASSWORD_WORDS", [])
#: If a password expired and the user wants to visit any
#: page a redirect is issued. By default, the URL the user
#: wanted to visit before is remembered and
#: stored as query string parameter called "next". If you
#: would prefer to use a different name for this parameter,
#: the :view:`PasswordChangeFormView` takes an optional
#: ``redirect_field_name`` keyword argument::
#:
#:    url(r'^/password_change/$',
#:        PasswordChangeFormView.as_view(redirect_field_name='previous'),
#:        name="password_change"),
#:
#: Note that if you provide a value to redirect_field_name, you
#: will most likely need to customize your :view:`PasswordChangeFormView`
#: template as well,
#: since the template context variable which stores the redirect
#: path will use the value of redirect_field_name as its key
#: rather than "next" (the default).
REDIRECT_FIELD_NAME = getattr(settings, "REDIRECT_FIELD_NAME", auth.REDIRECT_FIELD_NAME)
#: A path to a template to generate a 403 error page
#: in the root of the template directory.
TEMPLATE_403_PAGE = getattr(settings, "TEMPLATE_403_PAGE", "403.html")


PASSWORD_RESET_TIMEOUT_DAYS = 1

PASSWORD_POLICIES_LAST_CHECKED_SESSION_KEY = "_password_policies_last_checked"
PASSWORD_POLICIES_EXPIRED_SESSION_KEY = "_password_policies_expired"
PASSWORD_POLICIES_LAST_CHANGED_SESSION_KEY = "_password_policies_last_changed"
PASSWORD_POLICIES_CHANGE_REQUIRED_SESSION_KEY = "_password_policies_change_required"
