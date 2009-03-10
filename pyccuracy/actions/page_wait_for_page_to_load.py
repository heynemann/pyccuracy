from pyccuracy.errors import *
from pyccuracy.actions.action_base import *
from pyccuracy.actions.element_is_visible_base import *

class PageWaitForPageToLoadAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(PageWaitForPageToLoadAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["page_wait_for_page_to_load_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if not self.last_match: return ()

        timeout = float(self.last_match.groups()[2])
        return (timeout,)

    def execute(self, values, context):
        if (values):
            timeout = values[0]
            self.browser_driver.wait_for_page(timeout * 1000)
        else:
            self.browser_driver.wait_for_page()
