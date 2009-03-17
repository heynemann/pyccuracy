import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.actions.action_base import ActionBase
import re

class SearchGoogleAction(ActionBase):
    """
    Action that searches google for a given string.
    """

    def __init__(self, browser_driver, language):
        super(SearchGoogleAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = re.compile("^(And )?I search google for [\"](.+)[\"]$")
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return (self.last_match and (self.last_match.groups()[1],) or tuple([]))

    def execute(self, values, context):
        search_text = values[0]
        
        self.execute_action("I fill \"q\" textbox with \"%s\"" % search_text, context)
        self.execute_action("I click \"btnG\" button", context)

