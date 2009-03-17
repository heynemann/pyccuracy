import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.pyccuracy_core import *

class TestCustomActions(unittest.TestCase):

    def setUp(self):
        self.pyccuracy = PyccuracyCore()
                
    def test_search_google(self):
        custom_actions_dir = os.path.join(os.path.split(__file__)[0], "custom_actions")
        self.pyccuracy.run_tests(custom_actions_dir=custom_actions_dir, file_pattern="test_custom_action.acc")

if __name__ == "__main__":
    unittest.main()
