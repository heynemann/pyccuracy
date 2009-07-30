#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Bernardo Heynemann <heynemann@gmail.com>
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
#
# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.opensource.org/licenses/osl-3.0.php
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyccuracy.page import PageRegistry, Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

class RadioCheckAction(ActionBase):
    regex = LanguageItem("radio_check_regex")

    def execute(self, context, radio_key):
        element_type = "radio"
        element_key = self.resolve_element_key(context, element_type, radio_key)

        error_message = context.language.format("element_is_visible_failure", element_type, radio_key)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.radio_check(element_key)

class RadioIsCheckedAction(ActionBase):
    regex = LanguageItem("radio_is_checked_regex")

    def execute(self, context, radio_key):
        element_type = "radio"
        element_key = self.resolve_element_key(context, element_type, radio_key)

        error_messsage = context.language.format("element_is_visible_failure", element_type, radio_key)
        self.assert_element_is_visible(context, element_key, error_messsage)
        if not context.browser_driver.radio_is_checked(element_key):
            error_messsage = context.language.format("radio_is_checked_failure", radio_key)
            raise self.failed(error_messsage)

class RadioIsNotCheckedAction(ActionBase):
    regex = LanguageItem("radio_is_not_checked_regex")

    def execute(self, context, radio_key):
        element_type = "radio"
        element_key = self.resolve_element_key(context, element_type, radio_key)

        error_messsage = context.language.format("element_is_visible_failure", element_type, radio_key)
        self.assert_element_is_visible(context, element_key, error_messsage)
        if context.browser_driver.radio_is_checked(element_key):
            error_messsage = context.language.format("radio_is_not_checked_failure", radio_key)
            raise self.failed(error_messsage)


