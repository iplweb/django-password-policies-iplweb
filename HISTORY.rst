0.9.2
-----

* Add a ``__str__`` method to the ``PasswordChangeRequired`` model, returning a
  translatable ``"Password change required for user %s"`` description. Previously
  such objects rendered in the admin and in the shell as
  ``PasswordChangeRequired object (1)``, giving no clue which user they concerned
  (closes `#44 <https://github.com/iplweb/django-password-policies-iplweb/issues/44>`_).
  Thanks to `@dragondive <https://github.com/dragondive>`_ for the contribution
  (`#47 <https://github.com/iplweb/django-password-policies-iplweb/pull/47>`_).

0.9.1
-----

* Add support for Django 5.2 LTS, 6.0 and 6.1 — three series the package had
  fallen behind on; the supported matrix previously stopped at 5.1
* Drop end-of-life Django 5.0 and 5.1 from the CI matrix
* Fix the CI matrix actually testing the pinned Django version: ``uv run``
  re-synced the environment from the project metadata (``django>=4.2``) and
  silently replaced the version pinned by the preceding ``uv pip install``, so
  every cell was really testing the newest Django. ``uv run --no-sync`` plus an
  explicit ``uv sync`` makes the matrix mean what it says.

0.9
---

* Migrate packaging from setup.py to uv + pyproject.toml
* Migrate CI from Travis CI to GitHub Actions
* Replace pre-commit hooks with ruff
* Switch to setuptools-scm for version management
* Consolidate test and coverage config into pyproject.toml
* Rewrite README in Markdown with badges, version matrix, and install instructions
* Add ability to exclude specific users from password expiry and complexity checks
* Fix Sphinx docs: update for modern Django/Python, switch to RTD theme
* Add Read the Docs configuration (.readthedocs.yml)

0.8.6
-----

* Django 5 support
* default to JSONSerializer

0.8.4
-----

* fix password_reset_complete view (settings.LOGIN_URL problem)

0.8.3
-----

* correct buggy behaviour on password reset

0.8.2
-----

* corrected buggy behaviour when changed password of user without PasswordProfile entry
