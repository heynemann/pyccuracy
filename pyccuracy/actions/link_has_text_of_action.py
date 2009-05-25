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

import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class LinkHasTextOfAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(LinkHasTextOfAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["link_has_text_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])

    def execute(self, values, context):
        link_name = values[0]
        text = values[1]
        link = self.resolve_element_key(context, Page.Link, link_name)
        self.assert_element_is_visible(link, self.language["element_is_visible_failure"] % ("link", link_name))
        
        error_message = self.language["link_has_text_failure"]
        current_text = self.browser_driver.get_link_text(link)
        if text.lower() != current_text.lower():
            self.raise_action_failed_error(error_message % (link_name, text, current_text))

