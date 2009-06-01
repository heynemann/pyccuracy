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

class CheckboxCheckAction(ActionBase):
    regex = LanguageItem("checkbox_check_regex")
 
    def execute(self, context, *args, **kwargs):
        element_type = "checkbox"
        element_name = kwargs.get("checkbox_key", None)
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.checkbox_check(element_key)

class CheckboxIsCheckedAction(ActionBase):
    regex = LanguageItem("checkbox_is_checked_regex")

    def execute(self, context, *args, **kwargs):
        element_type = "checkbox"
        element_name = kwargs.get("checkbox_key", None)
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_messsage = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_messsage)
        if not context.browser_driver.checkbox_is_checked(element_key):
            error_messsage = context.language.format("checkbox_is_checked_failure", element_name)
            raise self.failed(error_messsage)


