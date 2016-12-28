#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='chatterbot_markov',
    version=0.1,
    description='Chatterbot Markov add on',
    author='PKnull',
    author_email='louis.grenzebach@gmail.com',
    url='https://github.com/pknull/chatterbot-markov',
    packages=[
        'chatterbot_markov',
    ],
    package_dir={'chatterbot-markov': 'chatterbot_markov'},
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    keywords='chatterbot-weather'
)