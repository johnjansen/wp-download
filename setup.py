#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from distutils.core import setup
from glob import glob

setup(name='wp-download',
      version='0.1.2b',
      description='Wikipedia database dump downloader',
      author='Wolodja Wentland',
      author_email='w@babilen5.org',
      url='http://github.com/babilen/wp-download',
      license='GPLv3',
      scripts=['scripts/wp-download'],
      long_description = open('doc/description.rst').read(),
      packages=['wp_download'],
      data_files=[
          ('share/doc/wp-download/examples/', ['examples/wpdownloadrc.sample']),
          ('share/doc/wp-download/doc', ['doc/Makefile','doc/README']),
          ('share/doc/wp-download/doc/rst', ['doc/rst/index.rst',
                                             'doc/rst/conf.py']),
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2 :: Only',
          'Programming Language :: Python :: 2.7',
          'Topic :: Database',
          'Topic :: Scientific/Engineering',
      ]
     )
