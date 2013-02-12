import os
from setuptools import setup, find_packages

import eca_catalogue


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-eca-catalogue',
    version=eca_catalogue.__version__,
    description='A reusable django app providing a generic product catalog for eComerce projects',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-eca-catalogue',
    packages=find_packages(),
    install_requires=[
        'django',
        'django-treebeard',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
        'PIL',
    ],
    test_suite='eca_catalogue.tests',
)
