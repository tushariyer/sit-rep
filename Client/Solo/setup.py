#!/usr/bin/env python

from distutils.core import setup

long_desc = 'Licensed under the generic MIT License.\"sit-rep\" can either be downloaded from the ' \
            'Releases page on GitHub and manually added to PATH or installed via \"pip\".'
version = ''

with open("Setup/version.txt", "r", encoding="utf-8") as fh:
    version = fh.read()
    fh.close()

setup(name='sit-rep-client',
      version=version,
      py_modules=['sit-rep-client'],
      description='Sit Rep [Client] | The System Situation Report',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      author='Tushar Iyer',
      author_email='',
      url='https://github.com/tushariyer/sit-rep',
      project_urls={
              "Bug Tracker": "https://github.com/tushariyer/sit-rep/issues",
          }
      )