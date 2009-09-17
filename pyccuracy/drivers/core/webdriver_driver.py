#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Bernardo Heynemann <heynemann@gmail.com>
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
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
from traceback import format_exc

from webdriver_firefox.webdriver import WebDriver

from pyccuracy.drivers.core.selenium_element_selector import *
from pyccuracy.drivers import BaseDriver, DriverError

class WebDriverDriver(BaseDriver):
    backend = 'webdriver'

    def __init__(self, context, selenium=None):
        self.context = context
        self.selenium = selenium

    def start_test(self, url=None):
        self.webdriver = WebDriver()

    def stop_test(self):
        self.webdriver.quit()

    def resolve_element_key(self, context, element_type, element_key):
        if not context:
            return element_key
        return SeleniumElementSelector.element(element_type, element_key)

    def page_open(self, url):
        self.webdriver.get(url)

    def wait_for_page(self, timeout=10000):
        # Does not make sense for WebDriver.
        pass

    def click_element(self, element_selector):
        self.webdriver.find_element_by_xpath(element_selector).click()

    def get_title(self):
        return self.webdriver.get_title()

    def is_element_visible(self, element_selector):
        try:
            element = self.webdriver.find_element_by_xpath(element_selector)
        except NoSuchElementException, e:
            return False
        except StaleElementReferenceException, e:
            return False
        except ElementNotVisibleException, e:
            return False
            
        return True

    def is_element_enabled(self, element_selector):
        return self.webdriver.find_element_by_xpath(element_selector).is_enabled()

    def wait_for_element_present(self, element_selector, timeout):
        elapsed = 0
        interval = 0.5

        while (elapsed < timeout):
            elapsed += interval
            if self.is_element_visible(element_selector):
                return True
            time.sleep(interval)

        return False

    def wait_for_element_to_disappear(self, element_selector, timeout):
        elapsed = 0
        interval = 0.5

        while (elapsed < timeout):
            elapsed += interval
            if not self.is_element_visible(element_selector):
                return True
            time.sleep(interval)

        return False

    def get_element_text(self, element_selector):
        return self.webdriver.find_element_by_xpath(element_selector).get_text()

    def get_element_markup(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        return self.webdriver.execute_script("argument[0].innerHTML", elem)

    #TODO
    def drag_element(self, from_element_selector, to_element_selector):
        pass
#        self.selenium.drag_and_drop_to_object(from_element_selector, to_element_selector)

    #TODO
    def mouseover_element(self, element_selector):
        pass
#        self.selenium.mouse_over(element_selector)

    #TODO
    def mouseout_element(self, element_selector):
        pass
#        self.selenium.mouse_out(element_selector)

    def checkbox_is_checked(self, checkbox_selector):
        return self.webdriver.find_element_by_xpath(checkbox_selector).is_selected()

    def checkbox_check(self, checkbox_selector):
        if not self.checkbox_is_checked(checkbox_selector):
            self.webdriver.find_element_by_xpath(checkbox_selector).toggle()

    def checkbox_uncheck(self, checkbox_selector):
        if self.checkbox_is_checked(checkbox_selector):
            self.webdriver.find_element_by_xpath(checkbox_selector).toggle()
    
    #TODO
    def get_selected_index(self, element_selector):
        pass
#        return int(self.selenium.get_selected_index(element_selector))

    #TODO
    def get_selected_value(self, element_selector):
        pass
#        return self.selenium.get_selected_value(element_selector)

    #TODO
    def get_selected_text(self, element_selector):
        pass
#        return self.selenium.get_selected_label(element_selector)

    #TODO
    def select_option_by_index(self, element_selector, index):
        pass
#        return self.__select_option(element_selector, "index", index)

    #TODO
    def select_option_by_value(self, element_selector, value):
        pass
#        return self.__select_option(element_selector, "value", value)

    #TODO
    def select_option_by_text(self, element_selector, text):
        pass
#        return self.__select_option(element_selector, "label", text)

    #TODO
    def __select_option(self, element_selector, option_selector, option_value):
        pass
#        error_message = "Option with %s '%s' not found" % (option_selector, option_value)
#        try:
#            self.selenium.select(element_selector, "%s=%s" % (option_selector, option_value))
#        except Exception, error:
#            if error.message == error_message:
#                return False
#            else:
#                raise
#        return True

    def is_element_empty(self, element_selector):
        current_text = self.webdriver.find_element_by_xpath(element_selector).get_text()
        return current_text == ""

    def get_image_src(self, image_selector):
        return self.__get_attribute_value(image_selector, "src")

    def type_text(self, input_selector, text):
        self.webdriver.find_element_by_xpath(input_selector).send_keys(text)

    def type_keys(self, input_selector, text):
        self.type_text(input_selector, text)

    def exec_js(self, js):
        self.driver.execute_script(js)

    def clean_input(self, input_selector):
        self.webdriver.find_element_by_xpath(input_selector).clear()

    def get_link_href(self, link_selector):
        return self.webdriver.find_element_by_xpath(link_selector).get_attribute("href")

    def get_html_source(self):
        return self.webdriver.get_page_source()

    def get_class(self, name):
        return self.__get_attribute_value(name, 'class')

    def get_xpath_count(self, xpath):
        return len(self.webdriver.find_elements_by_xpath(xpath))

    def __get_attribute_value(self, element, attribute):
        return self.webdriver.find_element_by_xpath(element).get_attribute(attribute)

    def radio_is_checked(self, radio_selector):
        return self.webdriver.find_element_by_xpath(radio_selector).is_selected()

    def radio_check(self, radio_selector):
        if not self.radio_is_checked(radio_selector):
            self.webdriver.find_element_by_xpath(radio_selector).set_selected()

    def radio_uncheck(self, radio_selector):
        raise NotImplementedError("Remove me! Does not make sense.")

