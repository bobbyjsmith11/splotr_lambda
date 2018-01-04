#!/usr/bin/env python
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = open(os.path.join(HERE, 'VERSION')).read().strip()

REQUIRED_PACKAGES = ['boto3',
                     'matplotlib',
                     'numpy',
                     'skrf']

setup(
    name='splotr_lambda',
    version=VERSION,
    description="Amazon lambda functions for Splotr application",
    author="Bobby Smith",
    author_email='bobbyjsmith11@gmail.com',
    url='',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    namespace_packages=['splotr_lambda'],
    install_requires=REQUIRED_PACKAGES,
    extras_require=dict(
        test=REQUIRED_PACKAGES + [
            'pytest>=3.2',
        ],
        develop=REQUIRED_PACKAGES + [
            'ipdb>=0.10.2',
        ]),
    zip_safe=False,
    dependency_links=[
    ],
)
