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

import time
import urllib2

class BrowserDriver(object):
    __browser__ = ""

    def __init__(self, browser_to_run, tests_dir):
        self.__browser__ = browser_to_run
        self.root_dir = tests_dir

    def resolve_element_key(self, context, element_type, element_key):
        raise NotImplementedError

    def __wait_for_server_to_start(self):
        server_started = False
        while server_started == False:
            server_started = self.__is_server_started()
            time.sleep(2)

    def __is_server_started(self):
        timeout = urllib2.socket.getdefaulttimeout()
        try:
            urllib2.socket.setdefaulttimeout(5)
            url = "http://%s:%s/" % (self.__host__, self.__port__)
            request = urllib2.urlopen(url)
            server_started = True
            request.close()
        except IOError, e:
            server_started = False

        urllib2.socket.setdefaulttimeout(timeout)
        return server_started

    def start(self):
        pass

    def get_xpath_count(self, xpath):
        raise NotImplementedError

    def get_class(self, name):
        """gets the css class name"""
        raise NotImplementedError

    def start_test(self, url = "http://www.someurl.com"):
        raise NotImplementedError

    def page_open(self, url):
        raise NotImplementedError

    def clean_input(self, input_selector):
        raise NotImplementedError

    def type(self, input_selector, text):
        raise NotImplementedError

    def click_element(self, element_selector):
        raise NotImplementedError

    def is_element_visible(self, element_selector):
        raise NotImplementedError

    def wait_for_page(self, timeout = 20000):
        raise NotImplementedError

    def get_title(self):
        raise NotImplementedError

    def is_element_enabled(self, element):
        raise NotImplementedError

    def checkbox_is_checked(self, checkbox_selector):
        raise NotImplementedError

    def checkbox_check(self, checkbox_selector):
        raise NotImplementedError

    def checkbox_uncheck(self, checkbox_selector):
        raise NotImplementedError

    def get_selected_index(self, element_selector):
        raise NotImplementedError

    def get_selected_value(self, element_selector):
        raise NotImplementedError

    def get_selected_text(self, element_selector):
        raise NotImplementedError

    def get_element_text(self, element_selector):
        raise NotImplementedError

    def get_element_markup(self, element_selector):
        raise NotImplementedError

    def select_option_by_index(self, element_selector, index):
        raise NotImplementedError

    def select_option_by_value(self, element_selector, value):
        raise NotImplementedError

    def select_option_by_text(self, element_selector, text):
        raise NotImplementedError

    def __select_option(self, element_selector, option_selector, option_value):
        raise NotImplementedError

    def get_link_href(self, link_selector):
        raise NotImplementedError

    def get_image_src(self, image_selector):
        raise NotImplementedError

    def get_link_text(self, link_selector):
        raise NotImplementedError

    def mouseover_element(self, element_selector):
        raise NotImplementedError

    def mouseout_element(self, element_selector):
        raise NotImplementedError

    def is_element_empty(self, element_selector):
        raise NotImplementedError

    def wait_for_element_present(self, element_selector, timeout):
        raise NotImplementedError

    def wait_for_element_to_disappear(self, element_selector, timeout):
        raise NotImplementedError

    def drag_element(self, from_element_selector, to_element_selector):
        raise NotImplementedError

    def stop_test(self):
        raise NotImplementedError

    def stop(self):
        pass

    def __get_attribute_value(self, element, attribute):
        raise NotImplementedError

