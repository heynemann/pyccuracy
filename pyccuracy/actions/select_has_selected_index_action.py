from element_is_visible_base import *
from element_selector import *
from action_base import *

class SelectHasSelectedIndexAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectHasSelectedIndexAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.select(element_name)

    def matches(self, line):
        reg = self.language["select_has_selected_index_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1], int(self.last_match.groups()[2])) or tuple([])

    def execute(self, values):
        select_name = values[0]
        index = values[1]

        select = self.get_selector(select_name)
        error_message = self.language["select_is_visible_failure"]
        selected_index = self.browser_driver.get_selected_index(select)

        if (selected_index != index):
            self.raise_action_failed_error(self.language["select_has_selected_index_failure"] % (select_name, index, selected_index))