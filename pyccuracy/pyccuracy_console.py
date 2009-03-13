#!/usr/bin/env python
# -*- coding: utf-8 -*
 
u"""Pyccuracy - BDD Acceptance testing

Example usage
=============
 
    python pyccuracy.py
 
:author: `Bernardo Heynemann <mailto:heynemann@gmail.com>`__
"""
 
# Pylint checks
# "line to long" pylint: disable-msg=C0301
# "Used * or ** magic" pylint: disable-msg=W0142
 
__revision__ = "$Id$"
__docformat__ = 'restructuredtext en'
 
import os, sys, optparse 
from pyccuracy_core import PyccuracyCore
 
def main():
    """ Main function - parses args and runs action """
    parser = optparse.OptionParser(usage="%prog or type %prog -h (--help) for help", description=__doc__, version="%prog" + __revision__)
    parser.add_option("-p", "--pattern", dest="pattern", default="*.acc", help="File pattern. Defines which files will get executed [default: %%default].")
    parser.add_option("-d", "--dir", dest="dir", default=os.curdir, help="Tests directory. Defines where the tests to be executed are [default: %%default]. Note: this is recursive, so all the tests under the current directory get executed.")
    parser.add_option("-u", "--url", dest="url", default=None, help="Base URL. Defines a base url against which the tests will get executed. For more details check the documentation [default: %%default].")
     
    (options, args) = parser.parse_args()

    pyc = PyccuracyCore()
    pyc.run_tests(file_pattern=options.pattern, tests_path=options.dir, base_url = options.url)
 
if __name__ == "__main__":
    main()
