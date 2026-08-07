0.9.4 (unreleased)
------------------

* Add ``__str__`` methods to the ``PasswordHistory`` and ``PasswordProfile``
  models, completing the work started for ``PasswordChangeRequired`` in 0.9.2.
  History entries and profiles rendered in the admin as
  ``PasswordHistory object (1)``; they now name the user, and history entries
  also carry their creation date, since a user has many of them.
* Drop the Django 1.x compatibility shims from ``password_policies.urls`` and
  use ``path()`` for the five static routes. The password reset confirmation
  route stays a ``re_path()`` — it passes its three components positionally and
  constrains their length, which ``path()`` converters cannot express. The
  published URLs are unchanged and are now pinned by tests.
* Fix the ruff configuration. ``W503`` was carried over from the old flake8
  config, but ruff has no such rule, and an unknown selector makes ruff abort
  before checking anything. The lint job in CI had therefore never linted a
  single line. Nine real violations it had been hiding are fixed, and the job
  no longer swallows its own exit code.

  Thanks to `@mikemanger <https://github.com/mikemanger>`_, whose
  `#39 <https://github.com/iplweb/django-password-policies-iplweb/pull/39>`_
  first pointed at all three of these.
* Publish to PyPI through Trusted Publishing (OIDC) instead of uploading by hand
  with a long-lived API token
  (`#53 <https://github.com/iplweb/django-password-policies-iplweb/pull/53>`_).
* Record the tree-wide ``ruff format`` commit in ``.git-blame-ignore-revs`` so
  ``git blame`` — and GitHub's blame view, which reads the file automatically —
  skips over it
  (`#55 <https://github.com/iplweb/django-password-policies-iplweb/pull/55>`_).

0.9.3
-----

* Fix the ``password_status`` context processor raising ``AttributeError`` when
  ``request`` carries no ``user``. This happens while Django renders the 500 page
  for an exception raised before ``AuthenticationMiddleware`` ran, and whenever a
  template is rendered outside the request/response cycle (``RequestFactory``,
  e-mails, management commands) — in the first case the crash masked the very
  exception being handled. The processor now returns an empty context instead,
  the same way Django guards ``django.contrib.auth.context_processors.auth``.
  Thanks to `@kostrom <https://github.com/kostrom>`_ for reporting and diagnosing
  it (`#21 <https://github.com/iplweb/django-password-policies-iplweb/pull/21>`_).
* Publish the Sphinx documentation to GitHub Pages at
  https://iplweb.github.io/django-password-policies-iplweb/, rebuilt from
  ``develop`` on every push, and link it from the README
  (`#51 <https://github.com/iplweb/django-password-policies-iplweb/pull/51>`_).

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
