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
from pyccuracy.errors import TestFailedError
from pyccuracy.pyccuracy_core import *

class TestInvalidUrl(unittest.TestCase):

    def setUp(self):
        self.pyccuracy = PyccuracyCore()

    def test_invalid_path_is_used(self):
        result = self.pyccuracy.run_tests(file_pattern="test_invalid_url.acc",
                                          should_throw=False,
                                          report_file_name="invalidurlreport.html")

        assert result.status == 'FAILED'
        assert result.failed_scenarios == 1

if __name__ == "__main__":
    unittest.main()
