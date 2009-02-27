from element_is_visible_base import *
from element_selector import *
from action_base import *

class CheckboxIsVisibleAction(ElementIsVisibleBase):
    def __init__(self, browser_driver, language):
        super(CheckboxIsVisibleAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.checkbox(element_name)

    def matches(self, line):
        reg = self.language["checkbox_is_visible_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        checkbox_name = values[0]
        error_message = self.language["checkbox_is_visible_failure"]
        self.execute_is_visible(checkbox_name, error_message)
