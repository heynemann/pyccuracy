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

import time
import re

selenium_available = True
# try:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
# except ImportError:
#     selenium_available = False

from pyccuracy.drivers import BaseDriver, DriverError
from selenium_element_selector import *

class SeleniumWebdriver(BaseDriver):
    backend = 'webdriver'

    def __init__(self, context):
        self.webdriver = None
        self.context = context
        if not selenium_available:
            raise RuntimeError('You *MUST* have selenium version 2+ installed to use the selenium webdriver')

    def start_driver(self):
        '''Create our driver instance'''
        host = self.context.settings.extra_args.get("selenium.server", "localhost")
        port = self.context.settings.extra_args.get("selenium.port", 4444)
        server_url = 'http://%s:%s/wd/hub' % (host, str(port))
        browser_to_run = self.context.settings.browser_to_run

        if hasattr(webdriver.DesiredCapabilities, browser_to_run.upper()):
            browser_to_run = getattr(webdriver.DesiredCapabilities, browser_to_run.upper())

        self.webdriver = webdriver.Remote(server_url, browser_to_run)


    def start_test(self, url=None):
        '''Start one task'''
        if not self.webdriver:
            self.start_driver()

        self.webdriver.get(url)

    def stop_test(self):
        '''Closes browser window.'''
        self.webdriver.quit()

    def exec_js(self, js):
        return self.webdriver.execute_script(js)

    def _get_element(self, element_selector):
        found_element = None
        if element_selector.startswith('//') or element_selector.startswith('xpath')  :
            found_element = self.webdriver.find_element_by_xpath(element_selector)
        else:
            found_element = self.webdriver.find_element_by_css_selector(element_selector)

        return found_element

    def resolve_element_key(self, context, element_type, element_key):
        return SeleniumElementSelector.element(element_type, element_key)

    def page_open(self, url):
        self.webdriver.get(url)

    def clean_input(self, input_selector):
        self._get_element(input_selector).clear()

    def type_text(self, input_selector, text):
        return self._get_element(input_selector).send_keys(text)

    def type_keys(self, input_selector, text):
        self.type_text(input_selector, text)

    def click_element(self, element_selector):
        return self._get_element(element_selector).click()

    def is_element_visible(self, element_selector):
        try:
            return self._get_element(element_selector).is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_page(self, timeout=30000):
        pass
        # the new recomendation from selenium is to watch for an element only
        # present with the new situation, all wait functions were dropped

    def get_title(self):
        return self.webdriver.title

    def is_element_enabled(self, element):
        return self._get_element(element).is_enabled()

    def checkbox_is_checked(self, checkbox_selector):
        return self._get_element(checkbox_selector).is_selected()

    def checkbox_check(self, checkbox_selector):
        check = self._get_element(checkbox_selector)
        if not check.is_selected():
            check.click()

    def checkbox_uncheck(self, checkbox_selector):
        check = self._get_element(checkbox_selector)
        if check.is_selected():
            check.click()

    def radio_is_checked(self, radio_selector):
        return self.checkbox_is_checked(radio_selector)

    def radio_check(self, radio_selector):
        return self.checkbox_check(radio_selector)

    def radio_uncheck(self, radio_selector):
        return self.checkbox_uncheck(radio_selector)

    def _get_select(self, select_selector):
        return Select(self._get_element(select_selector))

    def get_selected_index(self, element_selector):
        text = self.get_selected_text(element_selector)
        options = self.get_select_options(element_selector)
        return options.index(text)

    def get_selected_value(self, element_selector):
        return self._get_select(element_selector).first_selected_option.get_attribute('value')

    def get_selected_text(self, element_selector):
        return self._get_select(element_selector).first_selected_option.text

    def get_select_options(self, select):
        return [x.text for x in self._get_select(select).options]

    def get_element_text(self, element_selector):
        element = self._get_element(element_selector)
        tagname = element.get_attribute('tagName').lower()
        if tagname == 'input' or tagname == 'textarea':
            return element.get_attribute('value')
        else:
            return element.text

    def get_class(self, element_selector):
        return self._get_element(element_selector).get_attribute('className')

    def get_element_markup(self, element_selector):
        got = self._get_element(element_selector).get_attribute('innerHTML')
        return got != "null" and got or ""

    def get_html_source(self):
        return self.webdriver.page_source

    def select_option_by_index(self, element_selector, index):
        try:
            self._get_select(element_selector).select_by_index(index)
        except:
            return False
        return True

    def select_option_by_value(self, element_selector, value):
        try:
            self._get_select(element_selector).select_by_value(value)
        except:
            return False
        return True

    def select_option_by_text(self, element_selector, text):
        try:
            self._get_select(element_selector).select_by_visible_text(text)
        except:
            return False
        return True

    def get_link_href(self, link_selector):
        return self._get_element(link_selector).get_attribute('href')

    def get_image_src(self, image_selector):
        full_src = self._get_element(image_selector).get_attribute('src')
        # must return only filename
        src = re.sub(r'.*/','', full_src)
        return src

    def get_link_text(self, link_selector):
        return self._get_element(link_selector).text

    def mouseover_element(self, element_selector):
        chain = ActionChains(self.webdriver)
        chain.move_to_element(self._get_element(element_selector))
        chain.perform()

    def mouseout_element(self, element_selector):
        chain = ActionChains(self.webdriver)
        chain.move_by_offset(-10000,-10000)
        chain.perform()

    def is_element_empty(self, element_selector):
        return self.get_element_text(element_selector) == ""

    def wait_for_element_present(self, element_selector, timeout):
        elapsed = 0
        interval = 0.5

        while (elapsed < timeout):
            elapsed += interval
            try:
                elem = self._get_element(element_selector)
                if elem.is_displayed():
                    return True
            except NoSuchElementException:
                pass
            time.sleep(interval)

        return False

    def wait_for_element_to_disappear(self, element_selector, timeout):
        elapsed = 0
        interval = 0.5

        while (elapsed < timeout):
            elapsed += interval
            try:
                elem = self._get_element(element_selector)
            except NoSuchElementException:
                return True
            if not elem.is_displayed():
                return True
            time.sleep(interval)

        return False

    def drag_element(self, from_element_selector, to_element_selector):
        chain = ActionChains(self.webdriver)
        chain.drag_and_drop(self._get_element(from_element_selector),self._get_element(to_element_selector))
        chain.perform()

    def get_table_rows(self, table_selector):
        table = self._get_element(table_selector)
        rows = []
        row_elems = table.find_elements_by_tag_name('tr')

        for row_elem in row_elems:
            row = []
            cel_elems = row_elem.find_elements_by_tag_name('td')

            for cell_elem in cel_elems:
                row.append(cell_elem.text)

            rows.append(row)

        return rows

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "SeleniumWebdriver at '%s:%s' using '%s' browser." % (self.context.settings.extra_args.get("selenium.server", "localhost"),
                self.context.settings.extra_args.get("selenium.port", 4444),
                self.context.settings.browser_to_run)