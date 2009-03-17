import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class DivContainsTextAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(DivContainsTextAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["div_contains_text_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple()

    def execute(self, values, context):
        div_name = values[0]
        text = values[1]
        div = self.resolve_element_key(context, Page.Div, div_name)
        self.assert_element_is_visible(div, self.language["div_is_visible_failure"] % div_name)

        current_text = self.browser_driver.get_element_text(div)
        if (not current_text) or (not text in current_text):
            error_message = self.language["div_contains_text_failure"]
            self.raise_action_failed_error(error_message % (div_name, text, current_text))

