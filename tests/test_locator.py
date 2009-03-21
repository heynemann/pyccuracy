import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.locator import *

class TestLocator(unittest.TestCase):
    def __test_locate_test_files(self):
        files = list(locate("test*.py"))
        self.assertEqual(len(files), 8)

    def __test_locate_action_tests(self):
        files = list(locate("*en-us.acc"))
        self.assertEqual(len(files), 48)
        print files
        
if __name__ == "__main__":
    unittest.main()
