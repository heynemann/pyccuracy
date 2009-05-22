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

from page import Page

class SeleniumElementSelector(object):
    @staticmethod
    def element(element_type, element_name):
        method = getattr(SeleniumElementSelector, element_type, SeleniumElementSelector.generic)
        return method(element_name)

    @staticmethod
    def generic(element_name):
        '''
        Returns a xpath that matches a generic element
        '''
        return r"//*[(@name='%s' or @id='%s')]" % (element_name, element_name)        
        
    @staticmethod
    def button(element_name):
        '''
        Returns a regular expression that matches input type="button", input type="submit" or button tags with
        the specified argument as id or name.
        '''
        return r"//input[(@name='%s' or @id='%s') and (@type='button' or @type='submit')] | //button[@name='%s' or @id='%s']" % (element_name, element_name, element_name, element_name)
        
    @staticmethod
    def radio_button(element_name):
        '''
        Returns a regular expression that matches input type="radio" with the specified argument as id or name.
        '''
        return r"//input[(@name='%s' or @id='%s') and @type='radio']" % (element_name, element_name)

    @staticmethod
    def div(element_name):
        '''
        Returns a regular expression that matches div tags with
        the specified argument as id or name.
        '''
        return r"//div[(@name='%s' or @id='%s')]" % (element_name, element_name)

    @staticmethod
    def link(element_name):
        '''
        Returns a regular expression that matches link(a) tags with
        the specified argument as id or name.
        '''
        return r"//a[(@name='%s' or @id='%s')]" % (element_name, element_name)

    @staticmethod
    def checkbox(element_name):
        '''
        Returns a regular expression that matches input type="checkbox" tags with
        the specified argument as id or name.
        '''
        return r"//input[(@name='%s' or @id='%s') and @type='checkbox']" % (element_name, element_name)		

    @staticmethod
    def select(element_name):
        '''
        Returns a regular expression that matches Select tags with
        the specified argument as id or name.
        '''
        return r"//select[@name='%s' or @id='%s']" % (element_name, element_name)		

    @staticmethod
    def textbox(element_name):
        '''
        Returns a regular expression that matches input type="text", input without type attribute or textarea tags with
        the specified argument as id or name.
        '''
        return r"//input[(@name='%s' or @id='%s') and (@type='text' or not(@type))] | //textarea[@name='%s' or @id='%s']" % (element_name, element_name, element_name, element_name)

    @staticmethod
    def image(element_name):
        '''
        Returns a regular expression that matches img tags with
        the specified argument as id or name.
        '''
        return r"//img[@name='%s' or @id='%s']" % (element_name, element_name)
