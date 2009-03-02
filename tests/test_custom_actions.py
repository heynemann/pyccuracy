import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.pyccuracy_core import *

class TestCustomActions(unittest.TestCase):

    def setUp(self):
        self.pyccuracy = Pyccuracy()
                
    def __test_hello_world(self):
        custom_actions_dir = os.path.join(__file__, "custom_actions")
        self.pyccuracy.run_tests(custom_actions_dirs=(custom_actions_dir))

if __name__ == "__main__":
    unittest.main()
