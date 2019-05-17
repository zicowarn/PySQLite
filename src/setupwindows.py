#!/usr/bin/env python
# -*- coding: utf-8 -*-
# THIS IS PART OF Project 
# standardsqliteui.py - The core part of the PPROJECT for manger the sqlite databae,
# for export the sqlite table as sql file, or import a sql file into databse.
# 
# THIS PROGRAM IS FREE SOFTWARE, IS LICENSED UNDER MIT License
# You can redistribute it and/or modify it under the
# terms of the Do What The Want To  MIT License
# as published by Zhichao Wang. contact: ziccowarn@gmail.com for more details.
# 
# Copyright © 2018 Zhichao Wang <ziccowarn@gmail.com>
#
#


__author__ = 'Zhichao Wang'
__email__ = 'ziccowarn@gmail.com'
__version__ = '1.9.3'
__status__ = 'Beta'
__date__ = '2018-08-31'
__updated__ = '2019-05-02'


from distutils.core import setup
import py2exe  # @UnusedImport @UnresolvedImport
import os, sys  # @UnusedImport


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):  # @UnusedVariable
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
        break
    return paths


setup(
    name='standardsqliteui',
    version='1.9.3',
    # scripts=["settingmanagerui.py"],
    description="The Manager to select, import, export of sqlite database " ,
    author="Zhichao Wang" ,
    url=" http://www.me-iot.com" ,
    license="MIT" ,
    
    windows=[ 
        { 
            'script':'standardsqliteui.py',
            'icon_resources':[(1, '../images/Setup.ico')],
        }],

    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"],
                        'compressed': True,
                }
                },
    
    data_files=[ 
            ('images', ['../images/Setup.ico', '../images/PySQLitebrowser.ico']),
             ('', ['../Readme.md']),
            # for python distuils to generate a msi installer, please make the following two lines de-comment
            # ('DistExe/OpticamSettingManager', package_files(os.getcwd() + "/dist")),
            # ('DistExe/OpticamSettingManager/images', package_files(os.getcwd() + "/dist/images"))
            ],
    ) 
