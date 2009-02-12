from selenium import selenium
from selenium_browser_driver import *
import unittest
from pyccuracy_core import Pyccuracy

class TestStoryRunner(unittest.TestCase):
    svr = None
    
    def setUp(self):
        self.svr = SeleniumServer()        
        self.svr.run()
        
    def test_runner(self):
        pyc = Pyccuracy()
        pyc.run_tests()
        self.assertNotEquals(pyc,None)
        
    def tearDown(self):
        self.svr.stop()

if __name__ == "__main__":
    unittest.main()
