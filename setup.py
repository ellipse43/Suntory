#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):

    def run_tests(self):
        import tox
        errcode = tox.cmdline()
        sys.exit(errcode)


setup(
    name='Suntory',
    version='0.0.1',
    description='无敌是多么寂寞',
    author='ellipse42',
    author_email='ellipse42@qq.com',
    url='ellipse42.top',
    packages=find_packages(),
    include_package_data=True,
    tests_require=['tox'],
    cmdclass={'test': Tox},
)
