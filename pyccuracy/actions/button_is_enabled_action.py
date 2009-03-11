import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class ButtonIsEnabledAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(ButtonIsEnabledAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["button_is_enabled_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        button_name = values[0]		
        button = self.resolve_element_key(context, Page.Button, button_name)
        
        self.assert_element_is_visible(button, self.language["button_is_visible_failure"] % button_name)
        
        error_message = self.language["button_is_enabled_failure"]
        if not self.browser_driver.is_element_enabled(button):
            self.raise_action_failed_error(error_message % button_name)
