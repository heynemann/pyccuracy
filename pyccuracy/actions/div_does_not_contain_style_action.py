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

class DivDoesNotContainStyleAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(DivDoesNotContainStyleAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["div_does_not_contain_style_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple()

    def execute(self, values, context):
        div_name = values[0]
        style = values[1]
        div = self.resolve_element_key(context, Page.Div, div_name)
        self.assert_element_is_visible(div, self.language["element_is_visible_failure"] % ("div", div_name))
        current_style = self.browser_driver.get_class(div) or ""
        styles = current_style.split(" ")        
        if style in styles:
            error_message = self.language["div_does_not_contain_style_failure"]
            self.raise_action_failed_error(error_message % (div_name, style, current_style))

