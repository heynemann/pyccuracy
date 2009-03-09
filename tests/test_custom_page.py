import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.pyccuracy_core import PyccuracyCore

class TestCustomPage(unittest.TestCase):
    
    def test_runner(self):
        pyc = PyccuracyCore()
        pyc.run_tests(file_pattern="test_custom_page*.acc", page_folder=os.path.split(__file__)[0])
    
if __name__ == "__main__":
    unittest.main()
