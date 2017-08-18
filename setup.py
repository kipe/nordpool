#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='nordpool',
    version='0.02',
    description='Python library for fetching Nord Pool spot prices.',
    author='Kimmo Huoman',
    author_email='kipenroskaposti@gmail.com',
    url='https://github.com/kipe/nordpool',
    packages=[
        'nordpool',
    ],
    install_requires=[
        'python-dateutil>=2.6.1',
        'pytz>=2017.2',
        'requests>=2.18.4',
    ])
