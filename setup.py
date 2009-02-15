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

**Docs for current version**: http://packages.python.org/Pyccuracy/

=============
Release Notes
=============

Release Notes - Pyccuracy - Version 0.1
---------------------------------------
**Bug**

    [PYCCURACY-66 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-66] - Fix running the pyccuracy_core on *nix machines.

**New Feature**

    [PYCCURACY-14 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-14] - Check/Uncheck Checkbox Action
    [PYCCURACY-15 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-15] - Checkbox Is Checked Action
    [PYCCURACY-16 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-16] - Checkbox Is Not Checked Action
    [PYCCURACY-17 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-17] - See Checkbox Action
    [PYCCURACY-21 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-21] - See Button Action
    [PYCCURACY-40 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-40] - See Select Action
    [PYCCURACY-41 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-41] - Do Not See Select Action
    [PYCCURACY-42 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-42] - See Select Has Selected Index of Action
    [PYCCURACY-50 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-50] - Select Option By Index
    [PYCCURACY-57 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-57] - Click Image Action
    [PYCCURACY-58 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-58] - See Link Action
    [PYCCURACY-63 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-63] - Do Not See Link Action
    [PYCCURACY-64 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-64] - Click Link Action
    [PYCCURACY-80 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-80] - Render a summary of the run after the run
    [PYCCURACY-87 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-87] - Wait for Page To Load Action

**Task**

    [PYCCURACY-4 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-4] - Create documentation for current release
    [PYCCURACY-9 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-9] - Encapsulate Pyccuracy on a .egg
    [PYCCURACY-10 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-10] - Create index page for Pyccuracy.egg distribution
    [PYCCURACY-84 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-84] - Add tests for Click Button
    [PYCCURACY-85 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-85] - Add tests for Type Text
    [PYCCURACY-86 - http://jira.stormwindproject.org:8080/browse/PYCCURACY-86] - Add tests for See Title

""",
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
