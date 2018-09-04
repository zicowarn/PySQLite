#!/usr/bin/env python
# -*- coding: utf-8 -*-
# THIS IS PART OF Project 
# standardsqliteui.py - The core part of the PPROJECT for manger the sqlite databae,
# for export the sqlite table as sql file, or import a sql file into databse.
# 
# THIS PROGRAM IS FREE SOFTWARE, IS LICENSED UNDER MIT License
# You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To  MIT License
# as published by Zhichao Wang. contact: ziccowarn@gmail.com for more details.
# 
# Copyright © 2018 Zhichao Wang <ziccowarn@gmail.com>
#
#


__author__ = 'Zhichao Wang'
__email__ = 'ziccowarn@gmail.com'
__version__ = '1.9'
__status__ = 'Beta'
__date__ = '2018-09-04'
__updated__ = '2018-09-04'


from setuptools import setup
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):  # @UnusedVariable
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
        break
    return paths


APP = ['standardsqliteui.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

