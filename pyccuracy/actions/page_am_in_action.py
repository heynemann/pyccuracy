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
from os.path import abspath, join
import sys
sys.path.insert(0,abspath(__file__+"/../../../"))
from pyccuracy.common import URLChecker
from pyccuracy.errors import ActionFailedError
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *
from urllib import basejoin
import urllib2

import re

class PageAmInAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageAmInAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_am_in_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if not self.last_match: return tuple([])

        groups = self.last_match.groups()

        if groups[1] != None:
            return (groups[1].replace("\"", ""),)
        else:
            return (groups[2],)

    def execute(self, values, context):
        url = values[0]
        base_url = context.base_url

        if url.replace(" ", "") in context.all_pages:
            context.current_page = context.all_pages[url.replace(" ", "")]
            url = context.current_page.url
        else:
            raise self.language["page_am_in_failure"]
