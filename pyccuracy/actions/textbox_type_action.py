from pyccuracy.selenium_browser_driver import *
from element_selector import *
from action_base import *

class TextboxTypeAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(TextboxTypeAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.textbox(element_name)

    def matches(self, line):
        reg = self.language["textbox_type_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])

    def execute(self, values):
        textbox_name = values[0]
        text = values[1]
        textbox = self.get_selector(textbox_name)
        self.assert_element_is_visible(textbox, self.language["textbox_is_visible_failure"] % textbox_name)
        self.browser_driver.type(textbox, text)