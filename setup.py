#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Muduo

'''
    FastSync
'''
from setuptools import setup, find_packages

setup(
    name='FastSync',
    version='0.1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'watchdog',
        'pycrypto',
        'future'
    ],

    entry_points={
        'console_scripts': [
            'fsnd = src:sending',
            'frcv = src:receiving',
        ],
    },

    license='Apache License',
    author='Muduo',
    author_email='imuduo@163.com',
    url='https://github.com/iMuduo/FastSync',
    description='Event driven fast synchronization tool',
    keywords=['sync'],
)