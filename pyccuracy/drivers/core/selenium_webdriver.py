#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Iraê Carvalho <irae@irae.pro.br>
# Copyright (C) 2011 Luiz Tadao Honda <lhonda@yahoo-inc.com>
#
# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.opensource.org/licenses/osl-3.0.php
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

selenium_available = True
try:
    from selenium import webdriver
except ImportError:
    selenium_available = False

from pyccuracy.drivers import BaseDriver

class SeleniumWebdriver(BaseDriver):
    backend = 'webdriver'

    def __init__(self, context):
        self.webdriver = None
        self.selenium = None
        self.context = context
        if not selenium_available:
            raise RuntimeError('You *MUST* have selenium version 2+ installed to use the selenium webdriver')

    def start_driver(self):
        '''Create our driver instance'''
        host = self.context.settings.extra_args.get("selenium.server", "localhost")
        port = self.context.settings.extra_args.get("selenium.port", 4444)
        server_url = 'http://%s:%s/wd/hub' % (host, str(port))

        self.webdriver = webdriver.Remote(server_url, webdriver.DesiredCapabilities.FIREFOX)


    def start_test(self, url=None):
        '''Start one task'''
        if not self.webdriver:
            self.start_driver()

        self.webdriver.get(url)

    def stop_test(self):
        '''Closes browser window.'''
        self.webdriver.quit()

    def _get_element(self, element_selector):
        found_element = None
        if element_selector.startswith('//'):
            found_element = self.webdriver.find_element_by_xpath(element_selector)
        else:
            found_element = self.webdriver.find_element_by_css_selector(element_selector)

        return found_element

    def resolve_element_key(self, context, element_type, element_key):
        '''This method is responsible for transforming the element key for the given element type in something that the browser driver understands.

        i.e.:
            resolve_element_key(context, 'some', 'textbox')
            this method call would go into context, get the current page, verify the xpath or css selector for the specified element and then return it.

        You are free to implement this any way you'd like, though. One could implement this to return elements like:
            element type.element name as css selector, so a div with name myDiv would return div.myDiv.'''
        raise NotImplementedError

    def get_xpath_count(self, xpath):
        '''Returns the number of occurrences in the current document for the given xpath.'''
        raise NotImplementedError

    def page_open(self, url):
        self.webdriver.get(url)

    def clean_input(self, input_selector):
        '''This method wipes the text out of the given textbox'''
        raise NotImplementedError

    def type_text(self, input_selector, text):
        return self._get_element(input_selector).send_keys(text)

    def click_element(self, element_selector):
        return self._get_element(element_selector).click()

    def is_element_visible(self, element_selector):
        return self._get_element(element_selector).is_displayed()

    def wait_for_page(self, timeout=30000):
        pass

    def get_title(self):
        '''This method returns the title for the currently loaded document in the browser.'''
        raise NotImplementedError

    def is_element_enabled(self, element):
        '''This method returns whether the given element is enabled.'''
        raise NotImplementedError

    def checkbox_is_checked(self, checkbox_selector):
        '''This method returns whether the given checkbox is checked.'''
        raise NotImplementedError

    def checkbox_check(self, checkbox_selector):
        '''This method checks the specified checkbox.'''
        raise NotImplementedError

    def checkbox_uncheck(self, checkbox_selector):
        '''This method unchecks the specified checkbox.'''
        raise NotImplementedError

    def get_selected_index(self, element_selector):
        '''This method gets the selected index for the given select.'''
        raise NotImplementedError

    def get_selected_value(self, element_selector):
        '''This methid gets the value for the currently selected option in the given select.'''
        raise NotImplementedError

    def get_selected_text(self, element_selector):
        '''This methid gets the text for the currently selected option in the given select.'''
        raise NotImplementedError

    def get_element_text(self, element_selector):
        '''This method gets the text for the given element. This might mean different things for different element types (inner html for a div, value for a textbox, and so on).'''
        raise NotImplementedError

    def get_element_markup(self, element_selector):
        '''This method gets the given element markup.'''
        raise NotImplementedError

    def get_html_source(self):
        '''This method gets the whole source for the currently loaded document in the web browser.'''
        raise NotImplementedError

    def select_option_by_index(self, element_selector, index):
        '''This method selects an option in the given select by it's index.'''
        raise NotImplementedError

    def select_option_by_value(self, element_selector, value):
        '''This method selects the option that has the specified value in the given select.'''
        raise NotImplementedError

    def select_option_by_text(self, element_selector, text):
        '''This method selects the option that has the specified text in the given select.'''
        raise NotImplementedError

    def get_link_href(self, link_selector):
        '''This method returns the href attribute for the specified link.'''
        raise NotImplementedError

    def get_image_src(self, image_selector):
        '''This method returns the src attribute for the specified image.'''
        raise NotImplementedError

    def get_link_text(self, link_selector):
        '''This method gets the text for the specified link.'''
        raise NotImplementedError

    def mouseover_element(self, element_selector):
        '''This method triggers the mouse over event for the specified element.'''
        raise NotImplementedError

    def mouseout_element(self, element_selector):
        '''This method triggers the mouse out event for the specified element.'''
        raise NotImplementedError

    def is_element_empty(self, element_selector):
        '''This method returns whether the specified element has no text.'''
        raise NotImplementedError

    def wait_for_element_present(self, element_selector, timeout):
        '''This method waits for the given element to appear (become visible) or for the timeout. If it times out, the current scenario will fail.'''
        raise NotImplementedError

    def wait_for_element_to_disappear(self, element_selector, timeout):
        '''This method waits for the given element to disappear (become hidden or already be hidden) or for the timeout. If it times out, the current scenario will fail.'''
        raise NotImplementedError

    def drag_element(self, from_element_selector, to_element_selector):
        '''This method drags the from element to the to element.'''
        raise NotImplementedError

    def get_select_options(self, select):
        '''This method returns a list of options for the given select.'''
        raise NotImplementedError

    def get_table_rows(self, table_key):
        '''This method returns a list of rows for the given table.'''
        raise NotImplementedError


