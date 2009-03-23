import time
import urllib2
from browser_driver import *

class WebdriverBrowserDriver(BrowserDriver):
    __not_implemented_exception_message = "This method has not been implemented"

    def __init__(self, browser_to_run, tests_dir):
        super(type(self), self).__init__(browser_to_run, tests_dir)
        self.__port__ = 8888
        self.__host__ = 'localhost'

    def resolve_element_key(self, context, element_type, element_key):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def __wait_for_server_to_start(self):
        server_started = False
        while server_started == False:
            server_started = self.__is_server_started()
            time.sleep(2)

    def __is_server_started(self):
        timeout = urllib2.socket.getdefaulttimeout()
        try:
            urllib2.socket.setdefaulttimeout(5)
            url = "http://%s:%s/" % (self.__host, self.__port)
            request = urllib2.urlopen(url)
            server_started = True
            request.close()
        except IOError, e:
            server_started = False

        urllib2.socket.setdefaulttimeout(timeout)
        return server_started

    def start_test(self, url = "http://www.someurl.com"):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def page_open(self, url):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def type(self, input_selector, text):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def click_element(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def is_element_visible(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def wait_for_page(self, timeout = 20000):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_title(self):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def is_element_enabled(self, element):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def checkbox_is_checked(self, checkbox_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def checkbox_check(self, checkbox_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def checkbox_uncheck(self, checkbox_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_selected_index(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_selected_value(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_selected_text(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_element_text(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_element_markup(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def select_option_by_index(self, element_selector, index):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def select_option_by_value(self, element_selector, value):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def select_option_by_text(self, element_selector, text):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def __select_option(self, element_selector, option_selector, option_value):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_link_href(self, link_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_image_src(self, image_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def get_link_text(self, link_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def mouseover_element(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def is_element_empty(self, element_selector):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def stop_test(self):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

    def __get_attribute_value(self, element, attribute):
        raise ExceptionNotImplemented(self.__not_implemented_exception_message)

