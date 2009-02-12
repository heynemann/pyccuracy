from selenium import selenium
from selenium_browser_driver import *
import unittest
from pyccuracy_core import Pyccuracy

class TestStoryRunner(unittest.TestCase):
    
    def test_runner(self):
        pyc = Pyccuracy()
        pyc.run_tests()
    
if __name__ == "__main__":
    unittest.main()
