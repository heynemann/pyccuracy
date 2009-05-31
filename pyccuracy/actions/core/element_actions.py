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

from pyccuracy.page import PageRegistry, Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

class ElementClickAction(ActionBase):
    '''Clicks on a specific element.'''
    regex = LanguageItem('element_click_regex')

    def execute(self, context, *args, **kwargs):
        element_key = kwargs.get("element_key", None)
        element_type = kwargs.get("element_type", None)
        element_type = context.language.get(element_type.encode("utf-8") + "_category")
        should_wait = bool(kwargs.get("should_wait", None))

        element_key = self.resolve_element_key(context, element_type, element_key)

        #self.assert_element_is_visible(element_key, self.language.format("element_is_visible_failure", values["element_type"], element_name))
        context.browser_driver.click_element(element_key)

        if (should_wait):
            timeout = 10000
            try:
                context.browser_driver.wait_for_page(timeout=timeout)
            except Exception, error:
                if str(error) == "Timed out after %dms" % timeout:
                    self.raise_action_failed_error(context.language.format("timeout_failure", timeout))
                else:
                    raise
