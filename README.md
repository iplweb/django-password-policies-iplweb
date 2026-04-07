# django-password-policies-iplweb

[![Tests](https://github.com/iplweb/django-password-policies-iplweb/actions/workflows/main.yml/badge.svg)](https://github.com/iplweb/django-password-policies-iplweb/actions/workflows/main.yml)
[![PyPI Version](https://img.shields.io/pypi/v/django-password-policies-iplweb.svg)](https://pypi.org/project/django-password-policies-iplweb/)
[![Python Version](https://img.shields.io/pypi/pyversions/django-password-policies-iplweb.svg)](https://pypi.org/project/django-password-policies-iplweb/)
[![License](https://img.shields.io/pypi/l/django-password-policies-iplweb.svg)](LICENSE)

A Django application that provides unicode-aware password policies on password changes
and resets, along with a mechanism to force password changes.

Originally developed by Tarak Blah as
[django-password-policies](https://pypi.org/project/django-password-policies/).
This fork is actively maintained by [IPLweb](https://github.com/iplweb/).

<p align="center">
<b>Support graciously provided by</b><br><br>
<a href="https://www.iplweb.pl"><img src="https://www.iplweb.pl/images/ipl-logo-large.png" alt="IPLweb" width="150"></a>
</p>

## Why?

Django's built-in authentication provides basic password hashing and validation, but
lacks enterprise-grade password policy enforcement — expiration, reuse prevention,
forced rotation, and fine-grained complexity rules. This package fills that gap with
a pluggable, configurable set of policies that integrate with Django's auth system.

## Features

- **Password expiration** — automatically expire passwords after a configurable duration (default: 60 days)
- **Forced password changes** — redirect users to password change form via middleware, with admin bulk action support
- **Password history** — prevent reuse of the last N passwords (default: 10)
- **11 built-in validators** — letter/number/symbol counts, consecutive character limits, common sequence detection, entropy checks, dictionary lookup, cracklib support, email rejection
- **Password similarity check** — Levenshtein distance comparison between old and new passwords
- **Complete password change/reset views** — six class-based views with customizable templates and URLs
- **Django admin integration** — admin panels for password history and forced change management
- **26 configurable settings** — fine-tune every aspect of password policy enforcement
- **Context processor** — exposes `password_change_required` flag to templates
- **Unicode-aware** — full unicode support in password validation
- **I18N ready** — all user-facing messages use Django's translation framework

## Supported versions

| Django \ Python | 3.10 | 3.11 | 3.12 | 3.13 |
|-----------------|------|------|------|------|
| 4.2 LTS         | ✓    | ✓    | ✓    | ✗    |
| 5.0             | ✓    | ✓    | ✓    | ✓    |
| 5.1             | ✓    | ✓    | ✓    | ✓    |

## Installation

### Using uv (recommended)

```bash
uv add django-password-policies-iplweb
```

### Using pip

```bash
pip install django-password-policies-iplweb
```

## Quick start

Add to your Django settings:

```python
INSTALLED_APPS = [
    ...
    "password_policies",
]

MIDDLEWARE = [
    ...
    "password_policies.middleware.PasswordChangeMiddleware",
]

TEMPLATES = [
    {
        ...
        "OPTIONS": {
            "context_processors": [
                ...
                "password_policies.context_processors.password_status",
            ],
        },
    },
]
```

Run migrations:

```bash
python manage.py migrate password_policies
```

Include URLs:

```python
from django.urls import include, path

urlpatterns = [
    ...
    path("password/", include("password_policies.urls")),
]
```

## License

BSD-3-Clause — see [LICENSE](LICENSE) for details.
