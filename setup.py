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

Project Conventions: http://groups.google.com/group/pyccuracy/web/conventions

Links and Blog Posts: http://groups.google.com/group/pyccuracy/web/Links%20and%20Blog%20Posts

Project JIRA (Issue and Version Management) - 
http://jira.stormwindproject.org:8080/browse/PYCCURACY

Project Subversion Server: http://svn.stormwindproject.org/svn/Pyccuracy (``svn 
co http://svn.stormwindproject.org/svn/Pyccuracy Pyccuracy``)

**PyPI Page**: http://pypi.python.org/pypi/Pyccuracy/0.1dev-r879

**Docs for current version**: http://packages.python.org/Pyccuracy/

=============
Release Notes
=============

Release Notes - Pyccuracy - Version 0.1
---------------------------------------

**Bug**

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-66] - Fix 
running the 
pyccuracy_core on nix machines.

**New Feature**

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-14] - 
Check/Uncheck Checkbox Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-15] - 
Checkbox Is Checked Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-16] - 
Checkbox Is Not Checked Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-17] - 
See Checkbox Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-21] - 
See Button Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-40] - 
See Select Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-41] - 
Do Not See Select Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-42] - 
See Select Has Selected Index of Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-50] - 
Select Option By Index

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-57] - 
Click Image Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-58] - 
See Link Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-63] - 
Do Not See Link Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-64] - 
Click Link Action

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-80] - 
Render a summary of the run after the run

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-87] - 
Wait for Page To Load Action

**Task**

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-4] - 
Create documentation for current release

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-9] - 
Encapsulate Pyccuracy on a .egg

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-10] - 
Create index page for Pyccuracy.egg distribution

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-84] - 
Add tests for Click Button

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-85] - 
Add tests for Type Text

[http://jira.stormwindproject.org:8080/browse/PYCCURACY-86] - 
Add tests for See Title""",
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
