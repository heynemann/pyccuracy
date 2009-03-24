import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.pyccuracy_core import PyccuracyCore

class TestCatchInvalidScenarioError(unittest.TestCase):
    def setUp(self):
        self.pyccuracy = PyccuracyCore()
        
    def test_catch_invalid_scenario_error(self):
        self.pyccuracy.run_tests(file_pattern="test_catch_invalid_scenario_error_en-us.acc", pages_dir=os.path.split(__file__)[0], should_throw = False)
        self.pyccuracy.run_tests(file_pattern="test_catch_invalid_scenario_error_pt-br.acc", default_culture="pt-br", pages_dir=os.path.split(__file__)[0], should_throw = False)
    
if __name__ == "__main__":
    unittest.main()
