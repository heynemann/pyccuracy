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

from selenium import selenium
import unittest

class TestGoogle(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium("localhost", \
            4444, "*firefox", "http://www.google.com/")
        self.selenium.start()

    def test_google(self):
        sel = self.selenium
        sel.open("http://www.google.com/")
        sel.type("q", "hello world")
        sel.click("btnG")
        sel.wait_for_page_to_load(5000)
        self.assertEqual("hello world - Pesquisa Google", sel.get_title())

    def test_google_for_something(self):
        sel = self.selenium
        sel.open("http://www.google.com/")
        sel.type("q", "Something")
        sel.click("btnG")
        sel.wait_for_page_to_load(5000)
        self.assertEqual("Something - Pesquisa Google", sel.get_title())

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
