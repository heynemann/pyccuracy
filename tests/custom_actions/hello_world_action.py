import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_selector import ElementSelector

class HelloWorldAction(ActionBase):
    """
    Action that checks that a hello world text is present in txtHelloWorld.
    """

    def __init__(self, browser_driver, language):
        super(HelloWorldAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = r"^I see Hello World$"
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return ()

    def execute(self, values):
        textbox_name = "txtHelloWorld"
        text = "Hello World"
        textbox = ElementSelector.textbox(textbox_name)
        
        current_text = self.browser_driver.get_element_text(textbox)
        if (not current_text) or (not text.lower() == "hello world".lower()):
            self.raise_action_failed_error("No Hello World text found in txtHelloWorld")


