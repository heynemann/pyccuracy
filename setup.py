from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Pyccuracy',
      version=version,
      description="Pyccuracy is a BDD style Acceptance Testing framework",
      long_description="""\
============
Introduction
============

Pyccuracy is a BDD style Acceptance Testing framework.

===================
Project Cheat Sheet
===================

Project Google Groups Page - http://groups.google.com/group/pyccuracy
Project Conventions: Conventions

Links and Blog Posts: Links and Blog Posts

Project JIRA (Issue and Version Management) - http://jira.stormwindproject.org:8080/browse/PYCCURACY

Project Subversion Server: http://svn.stormwindproject.org/svn/Pyccuracy (``svn co http://svn.stormwindproject.org/svn/Pyccuracy Pyccuracy``)

**PyPI Page**: http://pypi.python.org/pypi/Pyccuracy/0.1dev-r879

**Docs for current version**: http://packages.python.org/Pyccuracy/""",
      classifiers=["Development Status :: 2 - Pre-Alpha",
				   "Intended Audience :: Developers",
				   "License :: OSI Approved",
				   "Natural Language :: English",
				   "Programming Language :: Python :: 2.5",
				   "Topic :: Software Development :: Testing",], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Acceptance Testing Accuracy Behavior Driven Development',
      author='Bernardo Heynemann',
      author_email='heynemann@gmail.com',
      url='http://www.pyccuracy.org',
      license='OSI',
      packages=["pyccuracy", "pyccuracy.actions"],
	  package_data = {
        'pyccuracy': ['languages/*.txt', 'lib/*/*.*', 'lib/*/*/*.*', 'lib/*/*/*/*.*'],
	  },
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "selenium>=0.9.2"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
