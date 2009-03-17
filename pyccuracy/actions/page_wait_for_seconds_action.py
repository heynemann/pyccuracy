import os
import sys
import time
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class PageWaitForSecondsAction(ActionBase):

    def matches(self, line):
        reg = self.language["page_wait_for_seconds_regex"]
        self.last_match = reg.search(line)

        return self.last_match

    def values_for(self, line):
        found_groups = self.last_match.groups()
        timeout = float(found_groups[1])
        return (timeout, )

    def execute(self, values, context):
        timeout = values[0]
        time.sleep(timeout)
