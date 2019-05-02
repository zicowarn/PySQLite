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
__updated__ = '2019-05-02'


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
APP_NANE = "PySQLite"
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': '../images/PySQLitebrowser.icns',
    'plist': {
        'CFBundleName': APP_NANE,
        'CFBundleDisplayName': APP_NANE,
        'CFBundleGetInfoString': "Pure Python SQLite Browser",
        'CFBundleIdentifier': "E1BFF42D-9CB2-4C0B-9882-C21245231893",
        'CFBundleVersion': "1.9 Beta",
        'CFBundleShortVersionString': "1.9",
        'NSHumanReadableCopyright': u"Copyright © 2019 " + __author__ + " All Rights Reserved"
    }
    
    }

setup(
    name=APP_NANE,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

