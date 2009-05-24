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

class TestPrePostScripts(unittest.TestCase):

    def setUp(self):
        self.pyccuracy = PyccuracyCore()

    def test_custom_pages(self):
        log_file = os.path.abspath(os.path.split(__file__)[0]) + "/pre_post_scripts_test.txt"
        self.clear_log_file(log_file)

        pyc = PyccuracyCore()
        self.pyccuracy.run_tests(file_pattern="pre_post_scripts_test.acc", pages_dir=os.path.split(__file__)[0], should_throw = True, report_file_name = "prepostscriptsreport.html")

        self.failUnless(os.path.exists(log_file), "The log file " + log_file + " was not found!")

        fsock = open(log_file, 'r')
        lines = fsock.readlines()
        fsock.close()

        first_line = "Pre Story - As a  Pyccuracy User I want to  test pre-post scripts So that  I can make sure Pyccuracy works"
        second_line = "Pre Scenario - Scenario 1 - Checking that files get added to disk"
        third_line = "Post Scenario - Scenario 1 - Checking that files get added to disk"
        fourth_line = "Post Story - As a  Pyccuracy User I want to  test pre-post scripts So that  I can make sure Pyccuracy works"

        self.failUnless(len(lines) == 4, "The log file should have 4 lines")
        self.failUnless(lines[0].strip() == first_line, "The first line should be \"%s\", but was \"%s\"" % (first_line, lines[0]))
        self.failUnless(lines[1].strip() == second_line, "The second line should be \"%s\", but was \"%s\"" % (second_line, lines[1]))
        self.failUnless(lines[2].strip() == third_line, "The third line should be \"%s\", but was \"%s\"" % (third_line, lines[2]))
        self.failUnless(lines[3].strip() == fourth_line, "The fourth line should be \"%s\", but was \"%s\"" % (fourth_line, lines[3]))

        self.clear_log_file(log_file)

    def clear_log_file(self, log_file):
        if os.path.exists(log_file):
            os.remove(log_file)

if __name__ == "__main__":
    unittest.main()
