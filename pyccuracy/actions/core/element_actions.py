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

def resolve_element_key(context, element_type, element_name, resolve_function):
    element_category = context.language.get(element_type.encode("utf-8") + "_category")
    return resolve_function(context, element_category, element_name)


class ElementClickAction(ActionBase):
    '''Clicks on a specific element.'''
    regex = LanguageItem('element_click_regex')

    def execute(self, context, *args, **kwargs):
        element_type = kwargs.get("element_type", None)
        element_name = kwargs.get("element_key", None)
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        should_wait = bool(kwargs.get("should_wait", None))


        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.click_element(element_key)

        if (should_wait):
            timeout = 10000
            try:
                context.browser_driver.wait_for_page(timeout=timeout)
            except Exception, error:
                if str(error) == "Timed out after %dms" % timeout:
                    raise self.failed(context.language.format("timeout_failure", timeout))
                else:
                    raise

class ElementIsVisibleAction(ActionBase):
    '''Asserts that a specific element is visible.'''
    regex = LanguageItem('element_is_visible_regex')

    def execute(self, context, *args, **kwargs):
        element_type = kwargs.get("element_type", None)
        element_name = kwargs.get("element_key", None)
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

class ElementIsNotVisibleAction(ActionBase):
    '''Asserts that a specific element is not visible.'''
    regex = LanguageItem('element_is_not_visible_regex')

    def execute(self, context, *args, **kwargs):
        element_type = kwargs.get("element_type", None)
        element_name = kwargs.get("element_key", None)
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_not_visible_failure", element_type, element_name)
        self.assert_element_is_not_visible(context, element_key, error_message)

class ElementIsEnabledAction(ActionBase):
    '''Asserts that a specific element is enabled.'''
    regex = LanguageItem('element_is_enabled_regex')

    def execute(self, context, *args, **kwargs):
        element_type = kwargs.get("element_type", None)
        element_name = kwargs.get("element_key", None)
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        if not context.browser_driver.is_element_enabled(element_key):
            error_message = context.language.format("element_is_enabled_failure", element_type, element_name)
            raise self.failed(error_message)

