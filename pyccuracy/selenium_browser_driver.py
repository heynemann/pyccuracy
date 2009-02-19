from selenium import *
from selenium_server import SeleniumServer
import time
import os
import urllib

class SeleniumBrowserDriver(object):
    def __init__(self, browser_to_run, tests_path):
        self.__host = "localhost"
        self.__port = 4444
        self.__browser = browser_to_run
        self.root_dir = tests_path

    def __wait_for_server_to_start(self):
        server_started = False
        while server_started == False: 
            try:
                url = "http://%s:%s/" % (self.__host, self.__port)
                request = urllib.urlopen(url)
                server_started = True
                request.close()
            except IOError, e:
                server_started = False
            time.sleep(2)

    def start(self):
        self.selenium_server = SeleniumServer()
        self.selenium_server.start()
        self.__wait_for_server_to_start()

    def start_test(self, url = "http://www.someurl.com"):
        self.selenium = selenium(self.__host, self.__port, self.__browser, url)
        self.selenium.start()

    def page_open(self, url):
        if self.is_url(url):
            self.selenium.open(url)
        else:
            new_url = os.path.join("file://" + os.path.abspath(self.root_dir), url)
            self.selenium.open(new_url)

    def type(self, input_selector, text):
        self.selenium.type(input_selector, text)

    def click_element(self, element_selector):
        self.selenium.click(element_selector)

    def is_element_visible(self, element_selector):
        return self.selenium.is_element_present(element_selector) and self.selenium.is_visible(element_selector)

    def wait_for_page(self, timeout = 20000):
        self.selenium.wait_for_page_to_load(timeout)

    def get_title(self):
        return self.selenium.get_title()
    
    def is_element_enabled(self, element):
        attr_value = self.__get_attribute_value(element, "disabled")
        return attr_value == None

    def checkbox_is_checked(self, checkbox_selector):
        return self.selenium.is_checked(checkbox_selector)

    def checkbox_check(self, checkbox_selector):
        self.selenium.check(checkbox_selector)

    def checkbox_uncheck(self, checkbox_selector):
        self.selenium.uncheck(checkbox_selector)

    def get_selected_index(self, checkbox_selector):
        return int(self.selenium.get_selected_index(checkbox_selector))

    def get_selected_value(self, checkbox_selector):
        return self.selenium.get_selected_value(checkbox_selector)

    def get_selected_text(self, checkbox_selector):
        return self.selenium.get_selected_text(checkbox_selector)

    def select_option_by_index(self, checkbox_selector, index):
        self.selenium.select(checkbox_selector, "index=%d" % index)

    def stop_test(self):
        self.selenium.stop()        

    def stop(self):
        self.selenium_server.stop()
        
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

    def is_url(self, url):
        url_regex = re.compile(r"^(?#Protocol)(?:(?:ht|f)tp(?:s?)\:\/\/|~/|/)?(?#Username:Password)(?:\w+:\w+@)?(?#Subdomains)(?:(?:[-\w]+\.)+(?#TopLevel Domains)(?:com|org|net|gov|mil|biz|info|mobi|name|aero|jobs|museum|travel|[a-z]{2}))(?#Port)(?::[\d]{1,5})?(?#Directories)(?:(?:(?:/(?:[-\w~!$+|.,=]|%[a-f\d]{2})+)+|/)+|\?|#)?(?#Query)(?:(?:\?(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)(?:&(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)*)*(?#Anchor)(?:#(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)?$")
        return url_regex.match(url)