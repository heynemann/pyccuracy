from selenium import selenium
from selenium_browser_driver import *
import unittest
from pyccuracy_core import Pyccuracy

class TestStoryRunner(unittest.TestCase):
    svr = None
    
    def setUp(self):
        print "setup -- 1"
        
        self.svr = SeleniumServer()        
        self.svr.run()
        print "setup -- fim"
    
    def test_runner(self):
        print "runner -- 1"
        pyc = Pyccuracy()
        pyc.run_tests()
        self.assertNotEquals(pyc,None)
        print "runenr -- fim"
        
    def tearDown(self):
        #self.svr.stop()
        pass

if __name__ == "__main__":
    unittest.main()
