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

class ElementIsVisibleBase(ActionBase):
    def __init__(self, browser_driver, language):
        super(ElementIsVisibleBase, self).__init__(browser_driver, language)

    def execute_is_visible(self, context, element_type, element_name, not_visible_message):
        element = self.resolve_element_key(context, element_type, element_name)
        self.assert_element_is_visible(element, not_visible_message % (element_type, element_name))

    def execute_is_not_visible(self, context, element_type, element_name, visible_message):
        element = self.resolve_element_key(context, element_type, element_name)
        self.assert_element_is_not_visible(element, visible_message % (element_type, element_name))
