import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.errors import *
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class PageSeeTitleAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageSeeTitleAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_see_title_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        expected_title = values[0]
        title = self.browser_driver.get_title()
        if (title != expected_title):
            self.raise_action_failed_error(self.language["page_see_title_failure"] % (title, expected_title))
