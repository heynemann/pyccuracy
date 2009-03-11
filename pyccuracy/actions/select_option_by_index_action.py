import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class SelectOptionByIndexAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectOptionByIndexAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["select_option_by_index_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (int(self.last_match.groups()[1]), self.last_match.groups()[2],) or tuple([])

    def execute(self, values, context):
        select_name = values[1]
        index = values[0]

        select = self.resolve_element_key(context, Page.Select, select_name)
        error_message = self.language["select_is_visible_failure"]
        self.assert_element_is_visible(select, error_message % select_name)        
        
        self.browser_driver.select_option_by_index(select, index)
        
