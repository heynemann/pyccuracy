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

from selenium import *

from pyccuracy.drivers import BaseDriver, DriverError
from selenium_element_selector import *

class SeleniumDriver(BaseDriver):
    backend = 'selenium'

    def __init__(self, context, selenium=None):
        self.context = context
        self.selenium = selenium

    def start_test(self, url=None):
        if not url:
            url = self.context.settings.base_url
        self.start_selenium(url)
        
    def start_selenium(self, url):
        host = self.context.settings.extra_args.get("selenium.server", "localhost")
        port = self.context.settings.extra_args.get("selenium.port", 4444)
        browser_to_run = self.context.settings.browser_to_run

        if not self.selenium:
            if not browser_to_run.startswith("*"):
                browser_to_run = "*%s" % browser_to_run
            self.selenium = selenium(host, port, browser_to_run, url)

        try:
            self.selenium.start()
        except Exception, e:
            raise DriverError("Error when starting selenium. Is it running?\n\n\n Error: %s\n" % format_exc(e))

    def stop_test(self):
        self.stop_selenium()
    
    def stop_selenium(self):
        self.selenium.stop()

    def resolve_element_key(self, context, element_type, element_key):
        if not context:
            return element_key
        return SeleniumElementSelector.element(element_type, element_key)

    def page_open(self, url):
        self.selenium.open(url)

    def wait_for_page(self, timeout=10000):
        self.selenium.wait_for_page_to_load(timeout)

    def click_element(self, element_selector):
        self.selenium.click(element_selector)

    def get_title(self):
        return self.selenium.get_title()

    def is_element_visible(self, element_selector):
        error_message = "ERROR: Element %s not found" % (element_selector)
        is_present = self.selenium.is_element_present(element_selector)
        if is_present:
            try:
                is_present = self.selenium.is_visible(element_selector)
            except Exception, error:
                if error.message == error_message:
                    is_present = False
                else:
                    raise
        return is_present

    def is_element_enabled(self, element):
        script = """this.page().findElement("%s").disabled;"""

        script_return = self.selenium.get_eval(script % element)
        if script_return == "null":
            is_disabled = self.__get_attribute_value(element, "disabled")
        else:
            is_disabled = script_return[0].upper()=="T" # is it 'True'?
        return not is_disabled

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
        text = ""
        tag_name_script = """this.page().findElement("%s").tagName;"""
        # escaping the user-made selector quotes
        element_selector = element_selector.replace('"', r'\"')
        tag_name = self.selenium.get_eval(tag_name_script % element_selector).lower()

        properties = {
                        "input" : "value",
                        "textarea" : "value",
                        "div" : "innerHTML"
                     }

        script = """this.page().findElement("%s").%s;"""
        try:
            # if the element is not in the dict above, I'll assume that we need to use "innerHTML"
            script_return = self.selenium.get_eval(script % (element_selector, properties.get(tag_name, "innerHTML")))
        except KeyError, err:
            raise ValueError("The tag for element selector %s is %s and Pyccuracy only supports the following tags: %s",
                             (element_selector, tag_name, ", ".join(properties.keys)))

        if script_return != "null":
            text = script_return

        return text

    def get_element_markup(self, element_selector):
        script = """this.page().findElement("%s").innerHTML;"""
        script_return = self.selenium.get_eval(script % element_selector)
        return script_return != "null" and script_return or ""

    def drag_element(self, from_element_selector, to_element_selector):
        self.selenium.drag_and_drop_to_object(from_element_selector, to_element_selector)

    def mouseover_element(self, element_selector):
        self.selenium.mouse_over(element_selector)

    def mouseout_element(self, element_selector):
        self.selenium.mouse_out(element_selector)

    def checkbox_is_checked(self, checkbox_selector):
        return self.selenium.is_checked(checkbox_selector)

    def checkbox_check(self, checkbox_selector):
        self.selenium.check(checkbox_selector)

    def checkbox_uncheck(self, checkbox_selector):
        self.selenium.uncheck(checkbox_selector)

    def get_selected_index(self, element_selector):
        return int(self.selenium.get_selected_index(element_selector))

    def get_selected_value(self, element_selector):
        return self.selenium.get_selected_value(element_selector)

    def get_selected_text(self, element_selector):
        return self.selenium.get_selected_label(element_selector)

    def select_option_by_index(self, element_selector, index):
        return self.__select_option(element_selector, "index", index)

    def select_option_by_value(self, element_selector, value):
        return self.__select_option(element_selector, "value", value)

    def select_option_by_text(self, element_selector, text):
        return self.__select_option(element_selector, "label", text)

    def get_select_options(self, element_selector):
        options = self.selenium.get_select_options(element_selector)
        return options

    def __select_option(self, element_selector, option_selector, option_value):
        error_message = "Option with %s '%s' not found" % (option_selector, option_value)
        try:
            self.selenium.select(element_selector, "%s=%s" % (option_selector, option_value))
        except Exception, error:
            if error.message == error_message:
                return False
            else:
                raise
        return True

    def is_element_empty(self, element_selector):
        current_text = self.get_element_text(element_selector)
        return current_text == ""

    def get_image_src(self, image_selector):
        return self.__get_attribute_value(image_selector, "src")

    def type_text(self, input_selector, text):
        self.selenium.type(input_selector, text)

    def type_keys(self, input_selector, text):
        self.selenium.type_keys(input_selector, text)

    def exec_js(self, js):
        return self.selenium.get_eval(js)

    def clean_input(self, input_selector):
        self.selenium.type(input_selector, "")

    def get_link_href(self, link_selector):
        return self.__get_attribute_value(link_selector, "href")

    def get_html_source(self):
        return self.selenium.get_html_source()

    def get_class(self, name):
        klass = self.__get_attribute_value(name, 'class')
        return klass

    def get_xpath_count(self, xpath):
        return self.selenium.get_xpath_count(xpath)

    def __get_attribute_value(self, element, attribute):
        try:
            locator = element + "/@" + attribute
            attr_value = self.selenium.get_attribute(locator)
        except Exception, inst:
            if "Could not find element attribute" in str(inst):
                attr_value = None
            else:
                raise
        return attr_value

    def radio_is_checked(self, radio_selector):
        return self.selenium.is_checked(radio_selector)

    def radio_check(self, radio_selector):
        self.selenium.check(radio_selector)

    def radio_uncheck(self, radio_selector):
        self.selenium.uncheck(radio_selector)
        
