from element_selector import *
from action_base import *

class TextboxContainsTextAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(TextboxContainsTextAction, self).__init__(browser_driver, language)

    def get_selector(self, element_name):
        return ElementSelector.textbox(element_name)

    def matches(self, line):
        reg = self.language["textbox_contains_text_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])

    def execute(self, values):
        textbox_name = values[0]
        text = values[1]
        textbox = self.get_selector(textbox_name)
        self.assert_element_is_visible(textbox, self.language["textbox_is_visible_failure"] % textbox_name)
        
        current_text = self.browser_driver.get_element_text(textbox)
        if (not current_text) or (not text in current_text):
            error_message = self.language["textbox_contains_text_failure"]
            self.raise_action_failed_error(error_message % (textbox_name, text, current_text))

