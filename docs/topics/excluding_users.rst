.. _excluding-users:

========================
Excluding specific users
========================

``django-password-policies-iplweb`` allows you to exclude specific users from
password policy enforcement by username. This is useful for service accounts,
bot users, or other automated accounts that should not be subject to password
policies.

Two separate settings control different aspects of the password policy:

.. _excluding-users-expiry:

Excluding users from password expiry
=====================================

To prevent specific users from being forced to change their password when it
expires, add their usernames to
``PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_USERNAMES`` in your Django settings::

    PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_USERNAMES = [
        "servicebot",
        "api_worker",
    ]

Users in this list will never be redirected to the password change page by the
:class:`~password_policies.middleware.PasswordChangeMiddleware`, even if their
password has expired or a
:class:`~password_policies.models.PasswordChangeRequired` entry exists.

.. note::
    This setting only affects the middleware. If an excluded user voluntarily
    visits the password change page, password complexity rules will still
    apply unless the user is also listed in
    ``PASSWORD_COMPLEXITY_EXCLUDED_USERNAMES``.

.. _excluding-users-complexity:

Excluding users from password complexity validation
====================================================

To allow specific users to set passwords without complexity validation
(character composition, entropy, dictionary checks, password history), add
their usernames to ``PASSWORD_COMPLEXITY_EXCLUDED_USERNAMES``::

    PASSWORD_COMPLEXITY_EXCLUDED_USERNAMES = [
        "servicebot",
        "api_worker",
    ]

Users in this list will not have their passwords validated against:

* Character composition rules (minimum letters, numbers, symbols)
* Entropy requirements
* Common sequence detection
* Dictionary word matching
* Password history (reuse prevention)

.. warning::
    Excluding users from complexity validation reduces the security of those
    accounts. Only add users to this list when there is a clear operational
    need, such as service accounts managed by automated systems.

.. _excluding-users-combining:

Combining both settings
========================

The two settings are independent. You can exclude a user from expiry checks
only, complexity checks only, or both::

    # This user is excluded from both expiry and complexity checks
    PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_USERNAMES = ["servicebot"]
    PASSWORD_COMPLEXITY_EXCLUDED_USERNAMES = ["servicebot"]

    # This user is only excluded from expiry (still gets complexity checks)
    PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_USERNAMES = ["api_worker"]

Both settings match against the username field (as returned by
``User.get_username()``). Both default to an empty list, preserving
backward compatibility.
