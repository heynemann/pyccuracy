from element_is_visible_base import *
from element_selector import *
from action_base import *

class LinkIsNotVisibleAction(ElementIsVisibleBase):
    def __init__(self, browser_driver, language):
        super(LinkIsNotVisibleAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.link(element_name)

    def matches(self, line):
        reg = self.language["link_is_not_visible_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        link_name = values[0]
        error_message = self.language["link_is_not_visible_failure"]
        self.execute_is_not_visible(link_name, error_message)