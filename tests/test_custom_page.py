import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.pyccuracy_core import PyccuracyCore

class TestCustomPage(unittest.TestCase):
    
    def setUp(self):
        self.languages_to_test = ("en-us","pt-br") #add more here as languages grow
        self.pyccuracy = PyccuracyCore()
    
    def test_custom_pages(self):
        pyc = PyccuracyCore()
        for language in self.languages_to_test:
            lang_pattern = "test_custom_page_%s.acc" % (language)
            self.pyccuracy.run_tests(file_pattern=lang_pattern, page_folder=os.path.split(__file__)[0])
    
if __name__ == "__main__":
    unittest.main()
