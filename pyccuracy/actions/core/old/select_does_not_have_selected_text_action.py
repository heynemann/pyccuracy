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
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class SelectDoesNotHaveSelectedTextAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectDoesNotHaveSelectedTextAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["select_does_not_have_selected_text_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1], self.last_match.groups()[2]) or tuple([])

    def execute(self, values, context):
        select_name = values[0]
        text = values[1]

        select = self.resolve_element_key(context, Page.Select, select_name)
        error_message = self.language["element_is_visible_failure"]
        self.assert_element_is_visible(select, error_message % ("select", select_name))
        
        selected_text = self.browser_driver.get_selected_text(select)

        if (selected_text.lower() == text.lower()):
            self.raise_action_failed_error(self.language["select_does_not_have_selected_text_failure"] % (select_name, text, selected_text))
