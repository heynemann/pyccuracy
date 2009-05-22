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

import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../"))
from pyccuracy.page import Page

class TestPageRegisteredElements(unittest.TestCase):
        
    def test_retrieve_element_by_key_only(self):
        page = Page()
        page.register_link("Algum link", "xpath")
        page.register_generic_element("li", "Generico", "xpath2")
        
        link = page.get_registered_element_by_key_only("Algum link")
        li = page.get_registered_element_by_key_only("Generico")
        
        self.failIf(link!="xpath", "O elemento com nome de Algum link deveria resolver para xpath mas resolveu para %s" % link)
        self.failIf(li!="xpath2", "O elemento com nome de Generico deveria resolver para xpath2 mas resolveu para %s" % li)
    
if __name__ == "__main__":
    unittest.main()
