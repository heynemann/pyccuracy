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
from pyccuracy.pyccuracy_core import *

class TestBaseUrl(unittest.TestCase):

    def setUp(self):
        self.pyccuracy = PyccuracyCore()
                
    def test_base_path_is_used(self):
        base_url = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "base_url_test")
        self.pyccuracy.run_tests(base_url = base_url, file_pattern = "test_base_url.acc", should_throw=True, report_file_name = "baseurlreport.html")

if __name__ == "__main__":
    unittest.main()
