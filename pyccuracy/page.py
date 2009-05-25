# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Page(object):
    '''Class that defines a page model.'''

    Button = "button"
    Checkbox = "checkbox"
    Div = "div"
    Image = "image"
    Link = "link"
    Page = "page"
    RadioButton = "radio_button"
    Select = "select"
    Textbox = "textbox"
    Element = '*'
    
    def __init__(self):
        '''Initializes the page with the given url.'''
        self.registered_elements = {}
        if hasattr(self, "register"): self.register()

    def get_registered_element(self, element_key):
        if not self.registered_elements.has_key(element_key): 
            return None
        return self.registered_elements[element_key]

    def register_element(self, element_key, element_locator):
        self.registered_elements[element_key] = element_locator

