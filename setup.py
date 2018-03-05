import os
from setuptools import find_packages, setup


# allow setup.py to be run from any path
def _get_description():
    try:
        path = os.path.join(os.path.dirname(__file__), 'README.rst')
        with open(path, encoding='utf-8') as f:
            return f.read()
    except IOError:
        return ''


setup(
    name='uk_geo_utils',
    version='0.1.0',
    author="chris48s",
    license="MIT",
    url="https://github.com/DemocracyClub/uk-geo-utils",
    packages=find_packages(),
    description='Django app for working with OS Addressbase, ONSUD and ONSPD',
    long_description=_get_description(),
    install_requires=[
        'Django',
        'psycopg2-binary',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
