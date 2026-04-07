0.9
---

* Migrate packaging from setup.py to uv + pyproject.toml
* Migrate CI from Travis CI to GitHub Actions
* Replace pre-commit hooks with ruff
* Switch to setuptools-scm for version management
* Consolidate test and coverage config into pyproject.toml
* Rewrite README in Markdown with badges, version matrix, and install instructions

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
