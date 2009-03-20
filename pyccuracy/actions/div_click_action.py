import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class DivClickAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(DivClickAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["div_click_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if self.last_match:
            groups = self.last_match.groups()
            return (groups[1], groups[2] is not None)
        else:
            return tuple([])

    def execute(self, values, context):
        div_name = values[0]
        div = self.resolve_element_key(context, Page.Div, div_name)
        self.assert_element_is_visible(div, self.language["div_is_visible_failure"] % div_name)
        self.browser_driver.click_element(div)

        if (values[1]):
            self.browser_driver.wait_for_page()
