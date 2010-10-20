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
import fudge

from pyccuracy import Page
from pyccuracy.common import Settings
from pyccuracy.errors import ActionFailedError
from pyccuracy.actions.core.element_actions import *

from ..utils import with_fudge

class FakeContext(object):
    settings = Settings(cur_dir='/')
    browser_driver = fudge.Fake('browser_driver')
    language = fudge.Fake('language')
    current_page = None

#Element Click Action

@with_fudge
def test_element_click_action_calls_the_right_browser_driver_methods():
    context = FakeContext()

    context.browser_driver.expects('resolve_element_key') \
                          .with_args(context, "button", "some") \
                          .returns("btnSome") \
                          .times_called(1)
    context.browser_driver.expects('is_element_visible') \
                          .with_args("btnSome") \
                          .returns(True) \
                          .times_called(1)
    context.browser_driver.expects('click_element') \
                          .with_args("btnSome") \
                          .times_called(1)

    context.language.expects('format') \
                          .with_args("element_is_visible_failure", "button", "some") \
                          .returns("button") \
                          .times_called(1)

    action = ElementClickAction()

    action.execute(context, element_name="some", element_type="button", should_wait=None)
