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

import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.page import Page

class TestCustomPage (Page):
    def register(self):
        self.url = "test_custom_page.htm"
        self.register_element("My Button", "//div[@class='something']/button[@class='button']")
        self.register_element("My Custom Checkbox", "//div[@class='something']/div[@name='other']/input[@type='checkbox' and @value='1']")
        self.register_element("Some Div", "//div[@class='something']/div[@name='other']")
        self.register_element("Some Image", "//img[@src='bogus_src']")
        self.register_element("My Link", "//a[@href='bogus_href']")
        self.register_element("Some Select", "//select[@alt='Some Select']")
        self.register_element("Some Textbox", "//div[contains(@class,'some')]//input[@type='text' and @class='textbox' and @name='some_textbox']")
