from element_selector import *
from action_base import *

class CheckboxIsNotCheckedAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(CheckboxIsNotCheckedAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.checkbox(element_name)

    def matches(self, line):
        reg = self.language["checkbox_is_not_checked_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        checkbox_name = values[0]
        checkbox = self.get_selector(checkbox_name)
        self.assert_element_is_visible(checkbox, self.language["checkbox_is_visible_failure"] % checkbox_name)
        if self.browser_driver.checkbox_is_checked(checkbox):
            self.raise_action_failed_error(self.language["checkbox_is_not_checked_failure"] % checkbox_name)