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

from re import compile as re_compile
from mocker import Mocker

from pyccuracy import Page
from pyccuracy.common import Settings
from pyccuracy.errors import ActionFailedError
from pyccuracy.actions.core.element_actions import *

from ..utils import assert_raises, Object

class FakeContext(object):
    def __init__(self, mocker):
        self.settings = Settings(cur_dir='/')
        self.browser_driver = mocker.mock()
        self.language = mocker.mock()
        self.current_page = None

def test_element_click_action_calls_the_right_browser_driver_methods():
    mocker = Mocker()
    
    context = FakeContext(mocker)
    
    context.browser_driver.resolve_element_key(context, "button", "some")
    mocker.result("btnSome")
    context.browser_driver.is_element_visible("btnSome")
    mocker.result(True)
    context.browser_driver.click_element("btnSome")
    
    context.language.format("element_is_visible_failure", "button", "some")
    mocker.result("button")
    context.language.get("button_category")
    mocker.count(min=0, max=None)
    mocker.result("button")
    
    with mocker:

        action = ElementClickAction()
    
        action.execute(context, element_name="some", element_type="button", should_wait=None)
