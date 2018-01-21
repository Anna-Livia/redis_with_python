#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name = 'RedisTweets',
    version = '0.2',
    author = 'Anna-Livia',
    author_email = 'contact@anna-livia.com',
    description = u'Creates a Twitter like app',

    install_requires = [
        'nose',
        'redis',
        ],

    test_suite = 'nose.collector',
    )