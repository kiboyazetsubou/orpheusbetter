#!/usr/bin/env python
'''
Installer script for apollobetter.
'''

from setuptools import setup
from _constants import __version__

setup(
    name = "apollobetter",
    description = "Automatically transcode and upload FLACs on apollo.rip.",
    author = 'Zach Denton',
    author_email = 'zacharydenton@gmail.com',
    version = __version__,
    url = 'https://github.com/sfunk1x/apollobetter',
    py_modules = [
        '_constants',
        'tagging',
        'transcode',
        'xanaxapi'
    ],
    scripts = ['apollobetter'],
    install_requires = [
        'mutagen',
        'mechanize',
        'requests'
    ]
)
