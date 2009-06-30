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
from pmock import *

from pyccuracy import Page
from pyccuracy.common import Settings
from pyccuracy.errors import ActionFailedError
from pyccuracy.actions.core.element_actions import *

from ..utils import assert_raises

class FakeContext(object):
    settings = Settings(cur_dir='/')
    browser_driver = Mock()
    language = Mock()
    current_page = None

#Element Click Action

def test_element_click_action_calls_the_right_browser_driver_methods():
    context = FakeContext()

    context.browser_driver.expects(once()) \
                          .resolve_element_key(same(context), eq("button"), eq("some")) \
                          .will(return_value("btnSome"))
    context.browser_driver.expects(once()) \
                          .is_element_visible(eq("btnSome")) \
                          .will(return_value(True))
    context.browser_driver.expects(once()) \
                          .click_element(eq("btnSome"))

    context.language.expects(once()) \
                    .format(eq("element_is_visible_failure"), eq("button"), eq("some")) \
                    .will(return_value("button"))

    context.language.expects(once()) \
                    .get(eq("button_category")) \
                    .will(return_value("button"))

    action = ElementClickAction()

    action.execute(context, element_name="some", element_type="button", should_wait=None)
    context.browser_driver.verify()
