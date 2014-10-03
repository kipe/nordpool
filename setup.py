#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='nordpool',
    version='0.01',
    description='Python library for Nordpool fetching spot prices.',
    author='Kimmo Huoman',
    author_email='kipenroskaposti@gmail.com',
    url='https://github.com/kipe/nordpool',
    packages=[
        'nordpool',
    ],
    install_requires=[
        'python-dateutil>=2.2',
        'pytz>=2014.7',
        'requests>=2.4.1',
    ])
