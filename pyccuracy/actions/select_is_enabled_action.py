import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class SelectIsEnabledAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectIsEnabledAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["select_is_enabled_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        select_name = values[0]		
        select = self.resolve_element_key(context, Page.Select, select_name)
        self.assert_element_is_visible(select, self.language["select_is_visible_failure"] % select_name)        
        
        error_message = self.language["select_is_enabled_failure"]
        if not self.browser_driver.is_element_enabled(select):
            self.raise_action_failed_error(error_message % select_name)
