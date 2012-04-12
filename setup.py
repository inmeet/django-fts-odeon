#/usr/bin/env python
import codecs
import os
import sys

from setuptools import setup, find_packages

if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

setup(
    name='django-fts-odeon',
    version='1.0',
    description='django-fts-odeon is a fork of django-fts ( http://code.google.com/p/django-fts/ ). The only supported back-end is PostgreSQL',
    long_description=read(os.path.join(os.path.dirname(__file__), 'README')),
    author='Stefan Talpalaru',
    author_email='developers@od-eon.com',
    url='http://github.com/inmeet/django-fts-odeon.git',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ],
)
