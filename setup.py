#!/usr/bin/env python

from distutils.core import setup

setup(
    name='harvest',
    version='1.0',
    description='A library for working with Harvest API (getharvest.com)',
    license='MIT',
    author='Alex Maslakov',
    author_email='me@gildedhonour.com, gilded.honour@gmail.com',
    url='https://www.github.com/harvest',
    packages=[''],
    long_description=open('README.md').read(),
    keywords = ['harvest-api', 'api', 'harvest-com', 'getharvest.com'], 
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],  
)