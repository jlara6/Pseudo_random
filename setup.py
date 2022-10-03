#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    name='pseudo_random',
    version='0.0.1',
    description="Python library for generating pseudo-random numbers",
    url='https://github.com/jlara6/pseudo_random',
    author="Jorge Lara",
    author_email='jlara@iee.unsj.edu.ar',
    license="BSD license",
    packages=find_packages(include=['pseudo_random', 'pseudo_random.*']),
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],    
    zip_safe=False,
)
