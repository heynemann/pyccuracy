#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

from pmock import *;

from pyccuracy.drivers.core.selenium_driver import SeleniumDriver
from pyccuracy.drivers import DriverError
from pyccuracy.common import Context, Settings
from utils import assert_raises

def test_can_create_selenium_browser_driver():
    context = Context(Settings())
    driver = SeleniumDriver(context)

    assert driver is not None

def test_selenium_driver_keeps_context():
    context = Context(Settings())
    driver = SeleniumDriver(context)

    assert driver.context == context

def test_selenium_driver_overrides_start_test_properly():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).start()

    driver = SeleniumDriver(context, selenium=selenium_mock)

    driver.start_test("http://localhost")
    selenium_mock.verify()

def test_selenium_driver_overrides_start_test_properly_when_extra_args_specified():
    context = Context(Settings())
    context.settings.extra_args = {
                                    "selenium.server":"localhost",
                                    "selenium.port":4444
                                  }
    selenium_mock = Mock()
    selenium_mock.expects(once()).start()

    driver = SeleniumDriver(context, selenium=selenium_mock)

    driver.start_test("http://localhost")
    selenium_mock.verify()

def test_selenium_driver_raises_on_start_test_when_selenium_cant_start():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).start().will(raise_exception(DriverError("invalid usage")))

    driver = SeleniumDriver(context, selenium=selenium_mock)

    assert_raises(DriverError, driver.start_test, url="http://localhost", exc_pattern=re.compile(r"Error when starting selenium. Is it running ?"))
    selenium_mock.verify()

def test_selenium_driver_calls_proper_selenese_on_stop_test():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).stop()

    driver = SeleniumDriver(context, selenium=selenium_mock)

    driver.stop_test()
    selenium_mock.verify()

def test_selenium_driver_overrides_page_open_properly():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).open(eq("http://localhost"))

    driver = SeleniumDriver(context, selenium=selenium_mock)

    driver.page_open("http://localhost")
    selenium_mock.verify()

def test_selenium_resolve_element_key_returns_element_key_for_null_context():
    driver = SeleniumDriver(None)
    assert driver.resolve_element_key(None, "button", "SomethingElse") == "SomethingElse"

def test_selenium_resolve_element_key_uses_SeleniumElementSelector_for_non_null_contexts():
    context = Context(Settings())
    driver = SeleniumDriver(context)
    key = driver.resolve_element_key(context, "Button", "SomethingElse")
    expected = "//*[(@name='SomethingElse' or @id='SomethingElse')]"
    assert key == expected, "Expected %s, Actual: %s" % (expected, key)

def test_selenium_driver_calls_proper_selenese_on_wait_for_page():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).wait_for_page_to_load(eq(30000))

    driver = SeleniumDriver(context, selenium=selenium_mock)

    driver.wait_for_page()
    selenium_mock.verify()

def test_selenium_driver_calls_proper_selenese_on_click_element():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).click(eq("some"))

    driver = SeleniumDriver(context, selenium=selenium_mock)

    driver.click_element("some")
    selenium_mock.verify()

def test_selenium_driver_calls_proper_selenese_on_get_title():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).get_title().will(return_value("Some title"))

    driver = SeleniumDriver(context, selenium=selenium_mock)

    title = driver.get_title()
    assert title == "Some title"
    selenium_mock.verify()
    
def test_selenium_driver_calls_get_eval():
    javascript = "some javascript"
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).get_eval(eq(javascript)).will(return_value("ok"))
    
    driver = SeleniumDriver(context, selenium=selenium_mock)
    
    assert driver.exec_js(javascript) == "ok"

def test_selenium_driver_calls_type_keys():
    input_selector = "//some_xpath"
    text = "text to type"
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).type_keys(eq(input_selector), eq(text))
    
    driver = SeleniumDriver(context, selenium=selenium_mock)
    driver.type_keys(input_selector, text)
    selenium_mock.verify()

def test_wait_for_presence():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).is_element_present(eq('some element')).will(return_value(True))
    selenium_mock.expects(once()).is_visible(eq('some element')).will(return_value(True))

    driver = SeleniumDriver(context, selenium=selenium_mock)
    driver.wait_for_element_present("some element", 1)
    selenium_mock.verify()

def test_wait_for_presence_works_even_when_is_visible_raises():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(at_least_once()).is_element_present(eq('some element')).will(return_value(True))
    selenium_mock.expects(once()).is_visible(eq('some element')).will(raise_exception(Exception("ERROR: Element some element not found"))).id("is_visible #1")
    selenium_mock.expects(once()).is_visible(eq('some element')).will(return_value(True)).after("is_visible #1")

    driver = SeleniumDriver(context, selenium=selenium_mock)
    driver.wait_for_element_present("some element", 1)
    selenium_mock.verify()

def test_wait_for_disappear():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(once()).is_element_present(eq('some element')).will(return_value(True))
    selenium_mock.expects(once()).is_visible(eq('some element')).will(return_value(False))

    driver = SeleniumDriver(context, selenium=selenium_mock)
    driver.wait_for_element_to_disappear("some element", 1)
    selenium_mock.verify()

def test_wait_for_disappear_works_even_when_is_visible_raises():
    context = Context(Settings())
    selenium_mock = Mock()
    selenium_mock.expects(at_least_once()).is_element_present(eq('some element')).will(return_value(True))
    selenium_mock.expects(once()).is_visible(eq('some element')).will(raise_exception(Exception("ERROR: Element some element not found")))

    driver = SeleniumDriver(context, selenium=selenium_mock)
    driver.wait_for_element_to_disappear("some element", 1)
    selenium_mock.verify()

