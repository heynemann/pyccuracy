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

class DriverInterface(object):
    """ This class contains only, those methods that must be
    implemented by browser drivers"""

    def start_test(self, url=None):
        '''This method is responsible for starting a test, whether this means opening a browser window, connecting to some remote server or anything else.
        
This method is called before any scenarios begin.'''
        raise NotImplementedError

    def stop_test(self):
        '''This method is responsible for cleaning up after a test run. This method is calledo only once after all scenarios are run.'''
        raise NotImplementedError

    def resolve_element_key(self, context, element_type, element_key):
        '''This method is responsible for transforming the element key for the given element type in something that the browser driver understands.
        
        i.e.:
            resolve_element_key(context, 'some', 'textbox')
            this method call would go into context, get the current page, verify the xpath or css selector for the specified element and then return it.
        
        You are free to implement this any way you'd like, though. One could implement this to return elements like:
            element type.element name as css selector, so a div with name myDiv would return div.myDiv.
'''
        raise NotImplementedError

    def get_xpath_count(self, xpath):
        '''Returns the number of occurrences in the current document for the given xpath.'''        
        raise NotImplementedError

    def page_open(self, url):
        raise NotImplementedError

    def clean_input(self, input_selector):
        raise NotImplementedError

    def type_text(self, input_selector, text):
        raise NotImplementedError

    def click_element(self, element_selector):
        raise NotImplementedError

    def is_element_visible(self, element_selector):
        raise NotImplementedError

    def wait_for_page(self, timeout=0):
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

    def get_html_source(self):
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

    def get_select_options(self, select):
        raise NotImplementedError
