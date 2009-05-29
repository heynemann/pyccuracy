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
from pyccuracy.locator import *

class TestLocator(unittest.TestCase):
    def __test_locate_test_files(self):
        files = list(locate("test*.py"))
        self.assertEqual(len(files), 8)

    def __test_locate_action_tests(self):
        files = list(locate("*en-us.acc"))
        self.assertEqual(len(files), 48)
        print files

if __name__ == "__main__":
    unittest.main()
