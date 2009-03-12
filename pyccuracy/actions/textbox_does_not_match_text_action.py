import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class TextboxDoesNotMatchTextAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(TextboxDoesNotMatchTextAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["textbox_does_not_match_text_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])

    def execute(self, values, context):
        textbox_name = values[0]
        text = values[1]
        textbox = self.resolve_element_key(context, Page.Textbox, textbox_name)
        self.assert_element_is_visible(textbox, self.language["textbox_is_visible_failure"] % textbox_name)
        
        current_text = self.browser_driver.get_element_text(textbox)
        if text.lower() == current_text.lower():
            error_message = self.language["textbox_does_not_match_text_failure"]
            self.raise_action_failed_error(error_message % (textbox_name, text, current_text))

