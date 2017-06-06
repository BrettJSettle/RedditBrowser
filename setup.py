#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme:
    LONG_DESCRIPTION = readme.read()


entry_points = """
[console_scripts]
redwall = redwall.main:main
"""

install_requires = [
      'beautifulsoup4',]

setup(name='redwall',
      version='0.0.1',
      description='A reddit wallpaper scraper',
      long_description=LONG_DESCRIPTION,
      author='Brett Settle',
      author_email='brettjsettle@gmail.com',
      install_requires=install_requires,
      license='MIT',
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Visualization',
          ],
      packages=find_packages(),
      entry_points=entry_points)








