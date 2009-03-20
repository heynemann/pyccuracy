import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.pyccuracy_core import *

class TestBaseUrl(unittest.TestCase):

    def setUp(self):
        self.pyccuracy = PyccuracyCore()
                
    def test_base_path_is_used(self):
        base_url = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "base_url_test")
        self.pyccuracy.run_tests(base_url = base_url, file_pattern = "test_base_url.acc", should_throw=True, report_file_name = "baseurlreport.html")

if __name__ == "__main__":
    unittest.main()
