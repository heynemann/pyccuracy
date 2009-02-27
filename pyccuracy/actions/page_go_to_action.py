from pyccuracy.selenium_browser_driver import *
from action_base import *

class PageGoToAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageGoToAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_go_to_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values):
        url = values[0]
        self.browser_driver.page_open(url)
        self.browser_driver.wait_for_page()