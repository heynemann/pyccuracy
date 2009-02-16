import re
from element_selector import *
from action_base import *

class SelectOptionByIndexAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectOptionByIndexAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.select(element_name)

    def matches(self, line):
        reg = self.language["select_option_by_index_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (int(self.last_match.groups()[1]), self.last_match.groups()[2],) or tuple([])

    def execute(self, values):
        select_name = values[1]
        index = values[0]

        select = self.get_selector(select_name)
        error_message = self.language["select_is_visible_failure"]
        self.browser_driver.select_option_by_index(select, index)
