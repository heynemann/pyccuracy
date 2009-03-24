import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase

class ElementOccursExactlyAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(type(self), self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["element_occurs_exactly_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        if self.last_match:
            groups = self.last_match.groups()
            return (groups[1], groups[2])
        else:
            return tuple([])

    def execute(self, values, context):
        element_name, expected_occurence = values[0], int(values[1])
        #import pdb;pdb.set_trace();
        element = self.resolve_element_key(context, Page.Any, element_name)

        times_occurred = int(self.browser_driver.count_element(element))
        error_message  = self.language["element_occurs_exactly_failure"]

        if times_occurred != expected_occurence:
            self.raise_action_failed_error(error_message %(element_name, expected_occurence, times_occurred))

        


