import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class PageWaitForPageToLoadAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageWaitForPageToLoadAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_wait_for_page_to_load_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if not self.last_match: return (-1,)
        found_groups = self.last_match.groups()
        if len(found_groups) < 4: return (-1,)
        timeout = float(found_groups[3])
        return (timeout,)

    def execute(self, values, context):
        timeout = values[0]
        if timeout == -1: timeout = None
        if timeout:
            self.browser_driver.wait_for_page(timeout * 1000)
        else:
            self.browser_driver.wait_for_page()
