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

u'''
Element actions can be used for any registered element (more about registering elements at "[[Creating custom Pages]]" section). The majority of Pyccuracy's actions are in this category, like clicking elements or verifying that they contain a given style.

Whenever you see element_name, it means the name of the registered element or the attribute "name" or "id" of the given element.

Whenever you see [element_type|element_selector] what this means is that you have to use one of the following:

h3. en-us:
  * button
  * radio button
  * div 
  * link 
  * checkbox 
  * select 
  * textbox 
  * image 
  * paragraph 
  * ul 
  * li
  * table
  * element (only use this if none of the above apply)

h3. pt-br:
  * botão 
  * radio 
  * div 
  * link 
  * checkbox 
  * select 
  * caixa de texto 
  * imagem 
  * parágrafo 
  * ul 
  * li
  * tabela
  * elemento (só utilize este se nenhum dos outro se aplicar)
  '''

from pyccuracy.page import PageRegistry, Page
from pyccuracy.actions import ActionBase
from pyccuracy.languages import LanguageItem

def resolve_element_key(context, element_type, element_name, resolve_function):
    element_type = element_type.encode("utf-8")
    resolved = resolve_function(context, element_type, element_name)
    if resolved:
        return resolved

    element_category = context.language.get(element_type + "_category")
    return resolve_function(context, element_category, element_name)

class ElementDoesNotContainStyleAction(ActionBase):
    '''h3. Examples

  * And I see "some" textbox does not have "width" style
  * And I see "other" button does not have "visible" style

h3. Description

This action asserts that the given element does not have the given style with any value.'''
    __builtin__ = True
    regex = LanguageItem('element_does_not_contain_style_regex')

    def execute(self, context, element_type, element_name, style_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_style = context.browser_driver.get_class(element_key) or ""
        styles = current_style.split(" ")

        if style_name in styles:
            error_message = context.language.format("element_does_not_contain_style_failure", element_type, element_name, style_name)
            raise self.failed(error_message)

class ElementContainsStyleAction(ActionBase):
    '''h3. Examples

  * And I see "some" textbox has "width" style
  * And I see "other" button has "visible" style

h3. Description

This action asserts that the given element has the given style with any value.'''
    __builtin__ = True
    regex = LanguageItem('element_contains_style_regex')

    def execute(self, context, element_type, element_name, style_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_style = context.browser_driver.get_class(element_key) or ""
        styles = current_style.split(" ")

        if style_name not in styles:
            error_message = context.language.format("element_contains_style_failure", element_type, element_name, style_name)
            raise self.failed(error_message)

class ElementClickAction(ActionBase):
    '''h3. Examples

  * And I click "some" button
  * And I click "other" checkbox and wait

h3. Description

This action instructs the browser driver to click the given element. If the "and wait" suffix is used, a "Wait for page to load" action is executed after this one.'''
    __builtin__ = True
    regex = LanguageItem('element_click_regex')

    def execute(self, context, element_type, element_name, should_wait):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

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
    '''h3. Examples

  * And I see "some" button
  * And I see "other" checkbox

h3. Description

This action asserts that the given element is visible.'''
    __builtin__ = True
    regex = LanguageItem('element_is_visible_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

class ElementIsNotVisibleAction(ActionBase):
    '''h3. Examples

  * And I do not see "some" button
  * And I do not see "other" checkbox

h3. Description

This action asserts that the given element is not visible.'''
    __builtin__ = True
    regex = LanguageItem('element_is_not_visible_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_not_visible_failure", element_type, element_name)
        self.assert_element_is_not_visible(context, element_key, error_message)

class ElementIsEnabledAction(ActionBase):
    '''h3. Examples

  * And I see "some" button is enabled
  * And I see "other" textbox is enabled

h3. Description

This action asserts that the given element is enabled.'''
    __builtin__ = True
    regex = LanguageItem('element_is_enabled_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        if not context.browser_driver.is_element_enabled(element_key):
            error_message = context.language.format("element_is_enabled_failure", element_type, element_name)
            raise self.failed(error_message)

class ElementIsDisabledAction(ActionBase):
    '''h3. Examples

  * And I see "some" button is disabled
  * And I see "other" textbox is disabled

h3. Description

This action asserts that the given element is disabled.'''
    __builtin__ = True
    regex = LanguageItem('element_is_disabled_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        if context.browser_driver.is_element_enabled(element_key):
            error_message = context.language.format("element_is_disabled_failure", element_type, element_name)
            raise self.failed(error_message)

class ElementWaitForPresenceAction(ActionBase):
    '''h3. Examples

  * And I wait for "some" button element to be present
  * And I wait for "other" textbox element to be present for 5 seconds

h3. Description

Waits until a given element appears or times out.

This action is really useful when you have some processing done (maybe AJAX) before an element is dynamically created.
'''
    __builtin__ = True
    regex = LanguageItem("element_wait_for_presence_regex")

    def execute(self, context, element_type, element_name, timeout):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        if not timeout:
            timeout = 5
        timeout = int(timeout)

        if not context.browser_driver.wait_for_element_present(element_key, timeout):
            error_message = context.language.format("element_wait_for_presence_failure", element_type, element_name, timeout, element_key)
            raise self.failed(error_message)

class ElementWaitForDisappearAction(ActionBase):
    '''h3. Examples

  * And I wait for "some" button element to disappear
  * And I wait for "other" textbox element to disappear for 5 seconds

h3. Description

Waits until a given element disappears (or is not visible already) or times out.

This action is really useful when you have some processing done (maybe AJAX) before an element is dynamically removed or hidden.
    '''
    __builtin__ = True
    regex = LanguageItem("element_wait_for_disappear_regex")

    def execute(self, context, element_type, element_name, timeout):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        if not timeout:
            timeout = 5
        timeout = int(timeout)

        if not context.browser_driver.wait_for_element_to_disappear(element_key, timeout):
            error_message = context.language.format("element_wait_for_disappear_failure", element_type, element_name, timeout, element_key)
            raise self.failed(error_message)

class ElementDragAction(ActionBase):
    '''h3. Example

  * I drag the "from" div to the "target" div

h3. Description

This action instructs the browser driver to drag the "from" element to the "target" element.'''
    __builtin__ = True
    regex = LanguageItem("element_drag_drop_regex")

    def execute(self, context, from_element_type, from_element_name, to_element_type, to_element_name):
        from_element_key = resolve_element_key(context, from_element_type, from_element_name, self.resolve_element_key)
        to_element_key = resolve_element_key(context, to_element_type, to_element_name, self.resolve_element_key)

        error_message = context.language.get("element_is_not_visible_for_drag_failure")
        self.assert_element_is_visible(context, from_element_key, error_message % from_element_key)
        self.assert_element_is_visible(context, to_element_key, error_message % to_element_key)

        context.browser_driver.drag_element(from_element_key, to_element_key)

class ElementContainsTextAction(ActionBase):
    '''h3. Example

  * I see "username" textbox contains "polo"

h3. Description

This action asserts that the text for the given element contains the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_contains_text_regex")

    def execute(self, context, element_type, element_name, text):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_text = context.browser_driver.get_element_text(element_key)
        if (not current_text) or (not text in current_text):
            error_message = context.language.format("element_contains_text_failure", element_type, element_name, text, current_text)
            raise self.failed(error_message)

class ElementDoesNotContainTextAction(ActionBase):
    '''h3. Example

  * I see "username" textbox does not contain "polo"

h3. Description

This action asserts that the text for the given element does not contain the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_does_not_contain_text_regex")

    def execute(self, context, element_type, element_name, text):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_text = context.browser_driver.get_element_text(element_key)
        if current_text and text in current_text:
            error_message = context.language.format("element_does_not_contain_text_failure", element_type, element_name, text, current_text)
            raise self.failed(error_message)

class ElementMatchesTextAction(ActionBase):
    '''h3. Example

  * I see "username" textbox matches "polo"

h3. Description

This action asserts that the text for the given element matches exactly the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_matches_text_regex")

    def execute(self, context, element_type, element_name, text):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_text = context.browser_driver.get_element_text(element_key)
        if (not current_text) or (text.strip() != current_text.strip()):
            error_message = context.language.format("element_matches_text_failure", element_type, element_name, text, current_text)
            raise self.failed(error_message)

class ElementDoesNotMatchTextAction(ActionBase):
    '''h3. Example

  * I see "username" textbox matches "polo"

h3. Description

This action asserts that the text for the given element does not match exactly the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_does_not_match_text_regex")

    def execute(self, context, element_type, element_name, text):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_text = context.browser_driver.get_element_text(element_key)
        if current_text and text.strip() == current_text.strip():
            error_message = context.language.format("element_does_not_match_text_failure", element_type, element_name, text, current_text)
            raise self.failed(error_message)

class ElementContainsMarkupAction(ActionBase):
    '''h3. Example

  * I see "username" textbox contains "&lt;p&gt;polo&lt;/p&gt;" markup

h3. Description

This action asserts that the markup for the given element contains the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_contains_markup_regex")

    def execute(self, context, element_type, element_name, markup):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_markup = context.browser_driver.get_element_markup(element_key)
        if (not current_markup) or (not markup in current_markup):
            error_message = context.language.format("element_contains_markup_failure", element_type, element_name, markup, current_markup)
            raise self.failed(error_message)

class ElementDoesNotContainMarkupAction(ActionBase):
    '''h3. Example

  * I see "username" textbox does not contain "&lt;p&gt;polo&lt;/p&gt;" markup

h3. Description

This action asserts that the markup for the given element does not contain the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_does_not_contain_markup_regex")

    def execute(self, context, element_type, element_name, markup):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_markup = context.browser_driver.get_element_markup(element_key)
        if current_markup and markup in current_markup:
            error_message = context.language.format("element_does_not_contain_markup_failure", element_type, element_name, markup, current_markup)
            raise self.failed(error_message)

class ElementMatchesMarkupAction(ActionBase):
    '''h3. Example

  * I see "username" textbox matches "&lt;p&gt;polo&lt;/p&gt;" markup

h3. Description

This action asserts that the markup for the given element matches exactly the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_matches_markup_regex")

    def execute(self, context, element_type, element_name, markup):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_markup = context.browser_driver.get_element_markup(element_key)
        if (not current_markup) or (markup.strip() != current_markup.strip()):
            error_message = context.language.format("element_matches_markup_failure", element_type, element_name, markup, current_markup)
            raise self.failed(error_message)

class ElementDoesNotMatchMarkupAction(ActionBase):
    '''h3. Example

  * I see "username" textbox does not match "&lt;p&gt;polo&lt;/p&gt;" markup

h3. Description

This action asserts that the markup for the given element does not match exactly the specified one.'''
    __builtin__ = True
    regex = LanguageItem("element_does_not_match_markup_regex")

    def execute(self, context, element_type, element_name, markup):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        current_markup = context.browser_driver.get_element_markup(element_key)
        if current_markup and markup.strip() == current_markup.strip():
            error_message = context.language.format("element_does_not_match_markup_failure", element_type, element_name, markup, current_markup)
            raise self.failed(error_message)

class ElementMouseoverAction(ActionBase):
    '''h3. Example

  * And I mouseover "some" image

h3. Description

This action instructs the browser driver to mouse over the specified element.'''
    __builtin__ = True
    regex = LanguageItem("element_mouseover_regex")

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.mouseover_element(element_key)

class ElementMouseOutAction(ActionBase):
    '''h3. Example

  * And I mouseout "some" image

h3. Description

This action instructs the browser driver to remove mouse focus from the specified element.'''
    __builtin__ = True
    regex = LanguageItem("element_mouseout_regex")

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.mouseout_element(element_key)
