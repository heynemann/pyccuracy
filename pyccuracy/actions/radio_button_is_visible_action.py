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
from pyccuracy.errors import ActionFailedError
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class RadioButtonIsVisibleAction(ElementIsVisibleBase):
    def __init__(self, browser_driver, language):
        super(RadioButtonIsVisibleAction, self).__init__(browser_driver, language)
    def matches(self, line):
        reg = self.language["radio_button_is_visible_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        radio_button_name = values[0]
        radio_button = self.resolve_element_key(context, Page.RadioButton, radio_button_name)
        
        if radio_button[0] == "/":
            count = int(self.browser_driver.get_xpath_count(radio_button_name))
            if count > 1:
                raise ActionFailedError(
                    self.language["radio_button_more_than_one_element_returned_failure"] % 
                                    (radio_button_name, radio_button, count))
        
        error_message = self.language["radio_button_is_visible_failure"]
        self.execute_is_visible(context, Page.RadioButton, radio_button_name, error_message)
