#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup


setup(
    name     = 'django-weeper',
    version  = '0.0.1',  # also update doc/conf.py:version
    packages = ['weeper'],
    install_requires=[
        "django-mailer",
    ],
    author       = 'Yakov Istomin',
    author_email = 'yakov@istomin.me',
)
