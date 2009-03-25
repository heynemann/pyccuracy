# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
