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

class ElementDragAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(ElementDragAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["element_drag_drop_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if self.last_match:
            from_element = self.last_match.group("from_element_key")
            from_element_type = self.last_match.group("from_element_type")
            to_element = self.last_match.group("to_element_key")
            to_element_type = self.last_match.group("to_element_type")
            return (from_element, from_element_type, to_element, to_element_type)
        else:
            return tuple([])

    def execute(self, values, context):
        from_element_key = values[0]
        from_element_type = values[1]
        to_element_key = values[2]
        to_element_type = values[3]

        from_element = self.resolve_element_key(context, from_element_type, from_element_key)
        to_element = self.resolve_element_key(context, to_element_type, to_element_key)
        self.assert_element_is_visible(from_element, self.language["element_is_not_visible_for_drag_failure"] % from_element_key)
        self.assert_element_is_visible(to_element, self.language["element_is_not_visible_for_drag_failure"] % to_element_key)

        self.browser_driver.drag_element(from_element, to_element)

