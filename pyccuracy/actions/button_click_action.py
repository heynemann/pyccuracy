from pyccuracy.selenium_browser_driver import *
from element_selector import *
from action_base import *

class ButtonClickAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(ButtonClickAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["button_click_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        button_name = values[0]
        button = ElementSelector.button(button_name)
        self.assert_element_is_visible(button, self.language["button_is_visible_failure"] % button_name)
        self.browser_driver.click_element(button)
        self.browser_driver.wait_for_page()