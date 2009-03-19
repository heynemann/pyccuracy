from setuptools import setup, find_packages
import sys, os

version = '0.3.2'

setup(name='Pyccuracy',
      version=version,
      description="Pyccuracy is a BDD style Acceptance Testing framework",
      long_description="""Pyccuracy is a Behavior-Driven Acceptance Testing framework (more on http://www.pyccuracy.org).""",
      classifiers=["Development Status :: 2 - Pre-Alpha",
				   "Intended Audience :: Developers",
				   "License :: OSI Approved",
				   "Natural Language :: English",
				   "Programming Language :: Python :: 2.5",
				   "Topic :: Software Development :: Testing",], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Acceptance Testing Accuracy Behavior Driven Development',
      author='Bernardo Heynemann',
      author_email='heynemann@gmail.com',
      url='http://groups.google.com/group/pyccuracy',
      license='OSI',
      packages=["pyccuracy", "pyccuracy.actions"],
	  package_data = {
        'pyccuracy': ['languages/*.txt', 'lib/*/*.*', 'lib/*/*/*.*', 'lib/*/*/*/*.*'],
	  },
      include_package_data=True,
      scripts = ['pyccuracy/pyccuracy_console.py'],
      zip_safe=True,
      install_requires=[
          "selenium>=0.9.2",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
