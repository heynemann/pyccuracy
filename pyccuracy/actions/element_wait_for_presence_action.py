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

class ElementWaitForPresenceAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(ElementWaitForPresenceAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["element_wait_for_presence_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if not self.last_match:
            return tuple()
        
        element_name = self.last_match.groups()[1]
        timeout = self.last_match.groups()[3] and float(self.last_match.groups()[3]) or 5
        return (element_name, timeout)

    def execute(self, values, context):
        element_name = values[0]
        timeout = values[1]
        element = self.resolve_element_key(context, Page.Element, element_name)

        if not self.browser_driver.wait_for_element_present(element, timeout):
            raise ActionFailedError(self.language['element_wait_for_presence_failure'] % (element_name, timeout))
