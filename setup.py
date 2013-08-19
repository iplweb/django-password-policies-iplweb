from setuptools import setup, find_packages

setup(
    name='password_policies',
    version=__import__('password_policies').__version__,
    description='A Django application to implent password policies.',
    long_description="""
django-password-policies is an application for the Django framework that
provides unicode-aware password policies on password changes and resets
and a mechanism to force password changes.
""",
    author='Tarak Blah',
    author_email='halbkarat@gmail.com',
    url='https://github.com/tarak/django-password-policies',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=['django<=1.6',
                      'django-easysettings',
    ],
    test_suite='tests.main',
)