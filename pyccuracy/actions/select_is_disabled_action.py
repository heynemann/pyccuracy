from element_selector import *
from action_base import *

class SelectIsDisabledAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(SelectIsDisabledAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.select(element_name)

    def matches(self, line):
        reg = self.language["select_is_disabled_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        link_name = values[0]		
        link = self.get_selector(link_name)
        self.assert_element_is_visible(link, self.language["select_is_visible_failure"] % link_name)        
        
        error_message = self.language["select_is_disabled_failure"]
        if not self.browser_driver.is_element_enabled(link):
            self.raise_action_failed_error(error_message % link_name)
