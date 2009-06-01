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

class SelectOptionByValueAction(ActionBase):
    regex = LanguageItem("select_option_by_value_regex")

    def execute(self, context, *args, **kwargs):
        select_name = kwargs.get("select_name", None)
        value = kwargs.get("option_value", None)
        select_key = resolve_element_key(context, Page.Select, select_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", Page.Select, select_name)
        self.assert_element_is_visible(context, select_key, error_message)
        
        result = context.browser_driver.select_option_by_value(select_key, value)
        
        if not result:
            error_message = context.language.format("select_option_by_value_failure", select_name, value)
            raise self.failed(error_message)

class SelectHasSelectedValueAction(ActionBase):
    regex = LanguageItem("select_has_selected_value_regex")

    def execute(self, context, *args, **kwargs):
        select_name = kwargs.get("select_name", None)
        value = kwargs.get("option_value", None)

        select = resolve_element_key(context, Page.Select, select_name, self.resolve_element_key)
        error_message = context.language.format("element_is_visible_failure", Page.Select, select_name)
        self.assert_element_is_visible(context, select, error_message)
        
        selected_value = context.browser_driver.get_selected_value(select)

        if (unicode(selected_value) != unicode(value)):
            error_message = context.language.format("select_has_selected_value_failure", select_name, value, selected_value)
            raise self.failed(error_message)

class SelectOptionByIndexAction(ActionBase):
    regex = LanguageItem("select_option_by_index_regex")

    def execute(self, context, *args, **kwargs):
        select_name = kwargs.get("select_name", None)
        index = int(kwargs.get("index", None))
        select_key = resolve_element_key(context, Page.Select, select_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", Page.Select, select_name)
        self.assert_element_is_visible(context, select_key, error_message)
        
        result = context.browser_driver.select_option_by_index(select_key, index)
        
        if not result:
            error_message = context.language.format("select_option_by_index_failure", select_name, index)
            raise self.failed(error_message)

class SelectHasSelectedIndexAction(ActionBase):
    regex = LanguageItem("select_has_selected_index_regex")

    def execute(self, context, *args, **kwargs):
        select_name = kwargs.get("select_name", None)
        index = kwargs.get("index", None)

        select = resolve_element_key(context, Page.Select, select_name, self.resolve_element_key)
        error_message = context.language.format("element_is_visible_failure", Page.Select, select_name)
        self.assert_element_is_visible(context, select, error_message)
        
        selected_index = context.browser_driver.get_selected_index(select)

        if (int(selected_index) != int(index)):
            error_message = context.language.format("select_has_selected_index_failure", select_name, index, selected_index)
            raise self.failed(error_message)

