# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# Check the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.actions.action_base import ActionBase

class PageCheckDoesNotContainMarkupAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageCheckDoesNotContainMarkupAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_check_does_not_contain_markup_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1], ) or tuple()

    def execute(self, values, context):
        expected_markup = values[0]
        html = self.browser_driver.get_html_source()

        if expected_markup in html:
            self.raise_action_failed_error(self.language["page_check_does_not_contain_markup_failure"] % expected_markup)
