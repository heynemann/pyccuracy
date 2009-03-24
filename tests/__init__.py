import os
import re
import sys
import unittest

from glob import glob

def get_test_modules():
    for filename in glob("tests/test_*.py"):
        filename = filename[6:-3]
        if re.search("^\w[\w_]+$", filename):
            module = __import__('tests.%s' % filename)
            yield unittest.TestLoader().loadTestsFromModule(getattr(module, filename))

def test_suite():
    return unittest.TestSuite([t for t in get_test_modules()])
