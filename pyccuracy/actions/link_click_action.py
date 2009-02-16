import re
from pyccuracy.selenium_browser_driver import *
from element_selector import *
from action_base import *

class LinkClickAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(LinkClickAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["link_click_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        link_name = values[0]
        link = ElementSelector.link(link_name)
        self.assert_element_is_visible(link, self.language["link_is_visible_failure"] % link_name)
        self.browser_driver.click_element(link)
        self.browser_driver.wait_for_page()