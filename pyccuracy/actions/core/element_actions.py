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
    element_type = element_type.encode("utf-8")
    resolved = resolve_function(context, element_type, element_name)
    if resolved:
        return resolved

    element_category = context.language.get(element_type + "_category")
    return resolve_function(context, element_category, element_name)

class ElementDoesNotContainStyleAction(ActionBase):
    '''Ensure that a specific element does not contain some style.'''
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
    '''Ensure that a specific element contains some style.'''
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
    '''Clicks on a specific element.'''
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
    '''Asserts that a specific element is visible.'''
    regex = LanguageItem('element_is_visible_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

class ElementIsNotVisibleAction(ActionBase):
    '''Asserts that a specific element is not visible.'''
    regex = LanguageItem('element_is_not_visible_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_not_visible_failure", element_type, element_name)
        self.assert_element_is_not_visible(context, element_key, error_message)

class ElementIsEnabledAction(ActionBase):
    '''Asserts that a specific element is enabled.'''
    regex = LanguageItem('element_is_enabled_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        if not context.browser_driver.is_element_enabled(element_key):
            error_message = context.language.format("element_is_enabled_failure", element_type, element_name)
            raise self.failed(error_message)

class ElementIsDisabledAction(ActionBase):
    '''Asserts that a specific element is disabled.'''
    regex = LanguageItem('element_is_disabled_regex')

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)

        if context.browser_driver.is_element_enabled(element_key):
            error_message = context.language.format("element_is_disabled_failure", element_type, element_name)
            raise self.failed(error_message)

class ElementWaitForPresenceAction(ActionBase):
    '''Waits until a given element appears or times out.'''
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
    '''Waits until a given element disappears (or is not visible already) or times out.'''
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
    regex = LanguageItem("element_drag_drop_regex")

    def execute(self, context, from_element_type, from_element_name, to_element_type, to_element_name):
        from_element_key = resolve_element_key(context, from_element_type, from_element_name, self.resolve_element_key)
        to_element_key = resolve_element_key(context, to_element_type, to_element_name, self.resolve_element_key)

        error_message = context.language.get("element_is_not_visible_for_drag_failure")
        self.assert_element_is_visible(context, from_element_key, error_message % from_element_key)
        self.assert_element_is_visible(context, to_element_key, error_message % to_element_key)

        context.browser_driver.drag_element(from_element_key, to_element_key)

class ElementContainsTextAction(ActionBase):
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
    regex = LanguageItem("element_mouseover_regex")

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.mouseover_element(element_key)

class ElementMouseOutAction(ActionBase):
    regex = LanguageItem("element_mouseout_regex")

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)

        error_message = context.language.format("element_is_visible_failure", element_type, element_name)
        self.assert_element_is_visible(context, element_key, error_message)
        context.browser_driver.mouseout_element(element_key)

