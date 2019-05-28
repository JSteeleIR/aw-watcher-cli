#!/usr/bin/env python

from setuptools import setup

# [No longer needed] Additional windows deps:
# - PyHook (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook)
# - pywin32 (`pip install pypiwin32`)

setup(name='aw-watcher-cli',
      version='0.1',
      description='Simple CLI "watcher" for ActivityWatch',
      author='Jacob Steele',
      author_email='jsteele@jsteeleir.com',
      url='https://github.com/jsteeleir/aw-watcher-cli',
      packages=['aw_watcher_cli'],
      entry_points={
          'console_scripts': ['aw-watcher-cli = aw_watcher_cli:main']
      },
      classifiers=[
          'Programming Language :: Python :: 3'
      ])

