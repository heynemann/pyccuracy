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
        host = self.context.settings.extra_args.get("selenium.server", "localhost")
        port = self.context.settings.extra_args.get("selenium.port", 4444)
        browser_to_run = self.context.settings.browser_to_run

        if not self.selenium:
            self.selenium = selenium(host, port, browser_to_run, url)

        try:
            self.selenium.start()
        except Exception, e:
            raise DriverError("Error when starting selenium. Is it running?\n\n\n Error: %s\n" % format_exc(e))

    def stop_test(self):
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

    def drag_element(self, from_element_selector, to_element_selector):
        self.selenium.drag_and_drop_to_object(from_element_selector, to_element_selector)

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
