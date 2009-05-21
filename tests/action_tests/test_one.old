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
from action_test_base import *

class TestOne(ActionTestBase):

    def set_pattern(self, pattern):
        self.pattern = pattern

    def get_pattern(self, culture):
        return "*%s_%s.acc" % (self.pattern, culture)

    def test_each_language(self, other):
        self.run_tests()

if __name__ == "__main__":
    test = TestOne("test_each_language")
    test.setUp()
    test.set_pattern(sys.argv[-1])
    runner = unittest.TextTestRunner()
    runner.run(test.test_each_language)

