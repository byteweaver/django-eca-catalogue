import os
from setuptools import setup, find_packages

import eca_catalogue


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-eca-catalogue',
    version=catalogue.__version__,
    description='A reusable django app providing a generic product catalog for E-comerce projects',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-eca-catalogue',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='catalogue.tests',
)
