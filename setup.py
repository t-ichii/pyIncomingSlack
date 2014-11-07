#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name          = 'pyIncomingSlack'
    ,version      = '0.1.1'
    ,description  = 'Post to Slack Channel/Groups using "Incoming WebHooks"'
    ,license      = 'MIT'
    ,author       = 'Takeru Ichii'
    ,author_email = 'takeru.ichii@facebook.com'
    ,url          = 'https://github.com/t-ichii/pyIncomingSlack'
    ,py_modules   = ['pyIncomingSlack']
    ,package_dir  = {'' : 'pyIncomingSlack'}
    ,entry_points = {
        "console_scripts": [
            "pyIncomingSlack=pyIncomingSlack:main"
        ]
    }
)

