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
from pyccuracy.actions.action_base import ActionBase
import re

class SearchGoogleAction(ActionBase):
    """
    Action that searches google for a given string.
    """

    def __init__(self, browser_driver, language):
        super(SearchGoogleAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = re.compile("^(And )?I search google for [\"](.+)[\"]$")
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return (self.last_match and (self.last_match.groups()[1],) or tuple([]))

    def execute(self, values, context):
        search_text = values[0]
        
        self.execute_action("I fill \"q\" textbox with \"%s\"" % search_text, context)
        self.execute_action("I click \"btnG\" button and wait", context)

