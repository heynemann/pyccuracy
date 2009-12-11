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

from webdriver_common.exceptions import *
from webdriver_firefox.webdriver import WebDriver

from pyccuracy.drivers import BaseDriver, DriverError
from pyccuracy.drivers.core.xpath_element_selector import *

class WebDriverDriver(BaseDriver):
    backend = 'webdriver'
    
    def __init__(self, context, webdriver=None):
        self.context = context
        self.webdriver = webdriver
    
    def start_test(self, url=None):
        self.webdriver = WebDriver()
    
    def stop_test(self):
        self.webdriver.quit()
	
    def resolve_element_key(self, context, element_type, element_key):
        if not context:
            return element_key
        return XPathElementSelector.element(element_type, element_key)
    
    def page_open(self, url):
        self.webdriver.get(url)
    
    def wait_for_page(self, timeout=10000):
        # Does not make sense for WebDriver because it always wait for page to load.
        pass
    
    def click_element(self, element_selector):
        self.webdriver.find_element_by_xpath(element_selector).click()
    
    def get_title(self):
        return self.webdriver.get_title()
    
    def check_css_style_is_visible(self, style):
        styles = style.split(';')
        for each_style in [s for s in styles if s != '']:
            name, value = each_style.split(':')
            name = name.strip().lower()
            value = value.strip().lower()
            if (name == 'visibility' and value == 'hidden') or (name == 'display' and value == 'none'):
                return False
        return True
    
    def is_element_visible(self, element_selector):
        try:
            element = self.webdriver.find_element_by_xpath(element_selector)
        except NoSuchElementException, e:
            return False
        except StaleElementReferenceException, e:
            return False
        except ElementNotVisibleException, e:
            return False
        
        try:
            style = element.get_attribute('style')
        except ErrorInResponseException, e:
            # if there was an error, assume that there's no style, 
            # therefore the element should be visible
            return True

        return self.check_css_style_is_visible(style)
    
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
        return self.webdriver.find_element_by_xpath(element_selector).get_value()
    
    def get_element_markup(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        return self.exec_js('argument[0].innerHTML', elem)
    
    def drag_element(self, from_element_selector, to_element_selector):
        raise NotImplementedError('Unfortunately Webdriver does not support drag-n-drop yet. ' + \
								   'If you really need it, you will have to use Selenium driver.')
    
    def mouseover_element(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        self.exec_js('argument[0].mouseover()', elem)
    
    def mouseout_element(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        self.exec_js('argument[0].mouseout()', elem)
    
    def checkbox_is_checked(self, checkbox_selector):
        return self.webdriver.find_element_by_xpath(checkbox_selector).is_selected()
    
    def checkbox_check(self, checkbox_selector):
        if not self.checkbox_is_checked(checkbox_selector):
            self.webdriver.find_element_by_xpath(checkbox_selector).toggle()
    
    def checkbox_uncheck(self, checkbox_selector):
        if self.checkbox_is_checked(checkbox_selector):
            self.webdriver.find_element_by_xpath(checkbox_selector).toggle()
    
    def get_selected_index(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        return self.exec_js('argument[0].selectedIndex;', elem)
    
    def get_selected_value(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        return self.exec_js('argument[0].options[argument[0].selectedIndex].value;', elem)
    
    def get_selected_text(self, element_selector):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        return self.exec_js('argument[0].options[argument[0].selectedIndex].innerText;', elem)
    
    def select_option_by_index(self, element_selector, index):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        self.exec_js('argument[0].selectedIndex = %d;' % index, elem)
    
    def select_option_by_value(self, element_selector, value):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        for index, option in enumerate(elem.find_elements_by_xpath('option')):
            if option.get_value() == value:
                self.select_option_by_index(element_selector, index)
    
    def select_option_by_text(self, element_selector, text):
        elem = self.webdriver.find_element_by_xpath(element_selector)
        for index, option in enumerate(elem.find_elements_by_xpath('option')):
            if option.get_text() == text:
                self.select_option_by_index(element_selector, index)
    
    def is_element_empty(self, element_selector):
        current_text = self.webdriver.find_element_by_xpath(element_selector).get_value()
        return current_text == ""
    
    def get_image_src(self, image_selector):
        return self.__get_attribute_value(image_selector, 'src')
    
    def type_text(self, input_selector, text):
        self.webdriver.find_element_by_xpath(input_selector).send_keys(text)
    
    def type_keys(self, input_selector, text):
        self.type_text(input_selector, text)
    
    def exec_js(self, js, *args):
        return self.webdriver.execute_script(js, *args)
    
    def clean_input(self, input_selector):
        self.webdriver.find_element_by_xpath(input_selector).clear()
    
    def get_link_href(self, link_selector):
        return self.webdriver.find_element_by_xpath(link_selector).get_attribute('href')
    
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
        raise NotImplementedError('Remove me! Does not make sense to uncheck a radio button; you will select another one.')

