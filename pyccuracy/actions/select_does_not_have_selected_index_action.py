import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class SelectDoesNotHaveSelectedIndexAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectDoesNotHaveSelectedIndexAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["select_does_not_have_selected_index_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1], int(self.last_match.groups()[2])) or tuple([])

    def execute(self, values, context):
        select_name = values[0]
        index = values[1]

        select = self.resolve_element_key(context, Page.Select, select_name)
        error_message = self.language["select_is_visible_failure"]
        self.assert_element_is_visible(select, self.language["select_is_visible_failure"] % select_name)
        
        selected_index = self.browser_driver.get_selected_index(select)

        if (selected_index == index):
            self.raise_action_failed_error(self.language["select_does_not_have_selected_index_failure"] % (select_name, index, selected_index))
