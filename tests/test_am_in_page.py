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

class TestAmInPage(unittest.TestCase):

    def setUp(self):
        self.languages_to_test = ("en-us")
        self.pyccuracy = PyccuracyCore()

    def test_am_in_page(self):
        result = self.pyccuracy.run_tests(file_pattern="test_am_in_page_en-us.acc",
                                          should_throw=False,
                                          report_file_name="test_am_in_page_report.html")

    def test_am_in_page_pt_br(self):
        result = self.pyccuracy.run_tests(file_pattern="test_am_in_page_pt-br.acc",
                                           should_throw=False,
                                           default_culture="pt-br",
                                           report_file_name="test_am_in_page_report.html")

if __name__ == "__main__":
    unittest.main()
