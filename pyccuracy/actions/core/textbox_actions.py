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

class TextboxIsEmptyAction(ActionBase):
    '''h3. Example

  * And I see "username" textbox is empty

h3. Description

This action asserts that the given textbox is empty.'''
    regex = LanguageItem("textbox_is_empty_regex")

    def execute(self, context, textbox_name):
        element_type = Page.Textbox
        element_key = self.resolve_element_key(context, element_type, textbox_name)

        error_message = context.language.format("element_is_visible_failure", "textbox", textbox_name)
        self.assert_element_is_visible(context, element_key, error_message)

        is_empty = context.browser_driver.is_element_empty(element_key)

        if not is_empty:
            error_message = context.language.format("textbox_is_empty_failure", textbox_name)
            raise self.failed(error_message)

class TextboxIsNotEmptyAction(ActionBase):
    '''h3. Example

  * And I see "username" textbox is not empty

h3. Description

This action asserts that the given textbox is not empty.'''
    regex = LanguageItem("textbox_is_not_empty_regex")

    def execute(self, context, textbox_name):
        element_type = "textbox"
        element_key = self.resolve_element_key(context, element_type, textbox_name)

        error_message = context.language.format("element_is_visible_failure", "textbox", textbox_name)
        self.assert_element_is_visible(context, element_key, error_message)

        is_empty = context.browser_driver.is_element_empty(element_key)

        if is_empty:
            error_message = context.language.format("textbox_is_not_empty_failure", textbox_name)
            raise self.failed(error_message)

class TextboxTypeAction(ActionBase):
    '''h3. Example

  * And I fill "details" textbox with "text"

h3. Description

This action types the given text in the given textbox.'''
    regex = LanguageItem("textbox_type_regex")

    def execute(self, context, textbox_name, text):
        textbox_key = self.resolve_element_key(context, Page.Textbox, textbox_name)

        error_message = context.language.format("element_is_visible_failure", "textbox", textbox_name)
        self.assert_element_is_visible(context, textbox_key, error_message)
        context.browser_driver.type_text(textbox_key, text)

class TextboxTypeSlowlyAction(ActionBase):
    '''h3. Example

  * And I slowly fill "details" textbox with "text"

h3. Description

This action types the given text in the given textbox. The difference between "slowly" typing and the regular typing is that this action raises javascript "key" events (keyUp, keyDown, etc).'''
    regex = LanguageItem("textbox_type_keys_regex")

    def execute(self, context, textbox_name, text):
        # Needed to work on Safari/Mac OS - Selenium bug?
        # I observed that it's only possible to type_keys after type_text once.
        TextboxTypeAction().execute(context, textbox_name, text)
        
        # now typyng slowly...
        textbox_key = self.resolve_element_key(context, Page.Textbox, textbox_name)
        context.browser_driver.type_keys(textbox_key, text)

class TextboxCleanAction(ActionBase):
    '''h3. Example

  * And I clean "details" textbox

h3. Description

This action cleans the given textbox (empties any text inside of it).'''
    regex = LanguageItem("textbox_clean_regex")

    def execute(self, context, textbox_name):
        textbox = self.resolve_element_key(context, Page.Textbox, textbox_name)

        error_message = context.language.format("element_is_visible_failure", "textbox", textbox_name)
        self.assert_element_is_visible(context, textbox, error_message)
        context.browser_driver.clean_input(textbox)
