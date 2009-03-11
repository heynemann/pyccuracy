import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class CheckboxIsCheckedAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(CheckboxIsCheckedAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["checkbox_is_checked_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        checkbox_name = values[0]
        checkbox = self.resolve_element_key(context, Page.Checkbox, checkbox_name)
        self.assert_element_is_visible(checkbox, self.language["checkbox_is_visible_failure"] % checkbox_name)
        if not self.browser_driver.checkbox_is_checked(checkbox):
            self.raise_action_failed_error(self.language["checkbox_is_checked_failure"] % checkbox_name)
