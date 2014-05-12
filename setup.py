#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup


setup(
    name='django-weeper',
    version='0.0.4',  # also update doc/conf.py:version
    packages=[
        'weeper',
        "weeper.management",
        "weeper.management.commands",
        "weeper.migrations",
    ],
    install_requires=[
        "django-mailer",
    ],
    author='Yakov Istomin',
    author_email='yakov@istomin.me',
    package_dir={"weeper": "weeper"},
    package_data={'weeper': [
        'locale/ru/LC_MESSAGES/*',
        'templates/admin/weeper/taskdelivery/*']},
)
