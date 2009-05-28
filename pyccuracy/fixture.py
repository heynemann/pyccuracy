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

from errors import *
import time
from test_result import *

from pyccuracy.fixture_items import *
from pyccuracy.common import TimedItem

class Fixture(TimedItem):
    def __init__(self):
        TimedItem.__init__(self)
        self.clear()

    def clear(self):
        self.invalid_test_files = []
        self.no_story_header = []
        self.stories = []

    def append_invalid_test_file(self, path, error):
        self.invalid_test_files.append((path, error))

    def append_no_story_header(self, path):
        self.no_story_header.append(path)

    def append_story(self, story):
        self.stories.append(story)
        return story

    def __str__(self):
        return self.get_results()
