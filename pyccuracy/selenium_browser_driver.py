import os
import sys
import time
import urllib2

from selenium import *
from browser_driver import *
from selenium_server import SeleniumServer
from selenium_element_selector import SeleniumElementSelector

class SeleniumBrowserDriver(BrowserDriver):
    def __init__(self, browser_to_run, tests_dir):
        super(type(self),self).__init__(browser_to_run, tests_dir)
        self.__port__ = 4444
        self.__host__ = "localhost"

    def resolve_element_key(self, context, element_type, element_key):
        if context == None: return element_key

        return SeleniumElementSelector.element(element_type, element_key)

    def start_test(self, url = "http://www.someurl.com"):
        self.selenium = selenium(self.__host__, self.__port__, self.__browser__, url)
        try:
            self.selenium.start()
        except Exception, e:
            sys.stderr.write("Error when starting selenium. Is it running ?\n")
            sys.exit(1)

    def page_open(self, url):
        self.selenium.open(url)

    def type(self, input_selector, text):
        self.selenium.type(input_selector, text)

    def clean_input(self, input_selector):
        self.selenium.type(input_selector, "")

    def click_element(self, element_selector):
        self.selenium.click(element_selector)

    def is_element_visible(self, element_selector):
        return self.selenium.is_element_present(element_selector) and self.selenium.is_visible(element_selector)

    def wait_for_page(self, timeout = 20000):
        self.selenium.wait_for_page_to_load(timeout)

    def get_title(self):
        return self.selenium.get_title()

    def is_element_enabled(self, element):
        script = """this.page().findElement("%s").disabled;"""

        script_return = self.selenium.get_eval(script % element)
        if script_return == "null":
            is_disabled = self.__get_attribute_value(element, "disabled")
        else:
            is_disabled = script_return[0].upper()=="T"
        return not is_disabled

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
        script_return = self.selenium.get_eval(script % (element_selector, properties[tag_name]))

        if script_return != "null":
            text = script_return        
        
        return text

    def get_element_markup(self, element_selector):
        script = """this.page().findElement("%s").innerHTML;"""
        script_return = self.selenium.get_eval(script % element_selector)
        return script_return != "null" and script_return or ""

    def select_option_by_index(self, element_selector, index):
        return self.__select_option(element_selector, "index", index)

    def select_option_by_value(self, element_selector, value):
        return self.__select_option(element_selector, "value", value)

    def select_option_by_text(self, element_selector, text):
        return self.__select_option(element_selector, "label", text)

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

    def get_link_href(self, link_selector):
        return self.__get_attribute_value(link_selector, "href")

    def get_image_src(self, image_selector):
        return self.__get_attribute_value(image_selector, "src")

    def get_link_text(self, link_selector):
        return self.selenium.get_text(link_selector)

    def mouseover_element(self, element_selector):
        self.selenium.mouse_over(element_selector)

    def is_element_empty(self, element_selector):
        current_text = self.get_element_text(element_selector)
        return current_text == ""

    def stop_test(self):
        self.selenium.stop()

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

