import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class ImageHasSrcOfAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(ImageHasSrcOfAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["image_has_src_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],self.last_match.groups()[2]) or tuple([])

    def execute(self, values, context):
        image_name = values[0]		
        src = values[1]
        image = self.resolve_element_key(context, Page.Image, image_name)
        self.assert_element_is_visible(image, self.language["image_is_visible_failure"] % image_name)        
        
        error_message = self.language["image_has_src_failure"]
        current_src = self.browser_driver.get_image_src(image)
        if src.lower() != current_src.lower():
            self.raise_action_failed_error(error_message % (image_name, src, current_src))

