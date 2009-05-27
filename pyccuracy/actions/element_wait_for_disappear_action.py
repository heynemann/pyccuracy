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

class ElementWaitForDisappearAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(ElementWaitForDisappearAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["element_wait_for_disappear_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match.groupdict()

    def execute(self, values, context):
        element_name = values["element_key"]
        element_type = values["element_type"]
        if (values.has_key("timeout") and values["timeout"]):
            timeout = int(values["timeout"])
        else:
            timeout = 5
        element = self.resolve_element_key(context, element_type, element_name)

        if not self.browser_driver.wait_for_element_to_disappear(element, timeout):
            raise ActionFailedError(self.language['element_wait_for_disappear_failure'] % (element_type, element_name, timeout))
