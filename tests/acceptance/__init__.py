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

import os
import re
import sys
import unittest

from glob import glob

def get_test_modules():
    for filename in glob("tests/test_*.py"):
        filename = filename[6:-3]
        if re.search("^\w[\w_]+$", filename):
            module = __import__('tests.%s' % filename)
            yield unittest.TestLoader().loadTestsFromModule(getattr(module, filename))

def test_suite():
    return unittest.TestSuite([t for t in get_test_modules()])
