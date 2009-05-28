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

from pyccuracy.page import Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

class PageSeeTitle(ActionBase):
    regex = LanguageItem('page_see_title_regex')

    def execute(self, values, context):
        expected_title = values[0]
        title = self.context.get_title()
        if (title != expected_title):
            raise PageSeeTitle.ActionFailedError(context.language.format("page_see_title_failure", title, expected_title))
