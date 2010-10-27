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

from mocker import Mocker

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
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.start()

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        driver.start_test("http://localhost")

def test_selenium_driver_overrides_start_test_properly_when_extra_args_specified():
    
    mocker = Mocker()
    
    context = Context(Settings())
    context.settings.extra_args = {
                                    "selenium.server":"localhost",
                                    "selenium.port":4444
                                  }
    selenium_mock = mocker.mock()
    selenium_mock.start()

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        driver.start_test("http://localhost")

def test_selenium_driver_raises_on_start_test_when_selenium_cant_start():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.start()
    mocker.throw(DriverError("invalid usage"))

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        assert_raises(DriverError, driver.start_test, url="http://localhost", \
                      exc_pattern=re.compile(r"Error when starting selenium. Is it running ?"))

def test_selenium_driver_calls_proper_selenese_on_stop_test():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.stop()

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        driver.stop_test()

def test_selenium_driver_overrides_page_open_properly():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.open("http://localhost")

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        driver.page_open("http://localhost")

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
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.wait_for_page_to_load(30000)

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        driver.wait_for_page()

def test_selenium_driver_calls_proper_selenese_on_click_element():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.click("some")

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        driver.click_element("some")

def test_selenium_driver_calls_proper_selenese_on_get_title():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.get_title()
    mocker.result("Some title")

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
    
        title = driver.get_title()
        assert title == "Some title"
    
def test_selenium_driver_calls_get_eval():
    
    mocker = Mocker()
    
    javascript = "some javascript"
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.get_eval(javascript)
    mocker.result("ok")
    
    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
        
        assert driver.exec_js(javascript) == "ok"

def test_selenium_driver_calls_type_keys():
    
    mocker = Mocker()
    
    input_selector = "//some_xpath"
    text = "text to type"
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.type_keys(input_selector, text)
    
    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
        driver.type_keys(input_selector, text)

def test_wait_for_presence():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.is_element_present('some element')
    mocker.result(True)
    selenium_mock.is_visible('some element')
    mocker.result(True)

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
        driver.wait_for_element_present("some element", 1)

def test_wait_for_presence_works_even_when_is_visible_raises():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.is_element_present('some element')
    mocker.count(min=1, max=None)
    mocker.result(True)
    
    with mocker.order():
        selenium_mock.is_visible('some element')
        mocker.throw(Exception("ERROR: Element some element not found"))
        selenium_mock.is_visible('some element')
        mocker.result(True)

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
        driver.wait_for_element_present("some element", 1)

def test_wait_for_disappear():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.is_element_present('some element')
    mocker.count(min=1, max=None)
    mocker.result(True)
    selenium_mock.is_visible('some element')
    mocker.count(min=1, max=None)
    mocker.result(True)

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
        driver.wait_for_element_to_disappear("some element", 1)

def test_wait_for_disappear_works_even_when_is_visible_raises():
    
    mocker = Mocker()
    
    context = Context(Settings())
    selenium_mock = mocker.mock()
    selenium_mock.is_element_present('some element')
    mocker.count(min=1, max=None)
    mocker.result(True)
    selenium_mock.is_visible('some element')
    mocker.throw(Exception("ERROR: Element some element not found"))

    with mocker:
        driver = SeleniumDriver(context, selenium=selenium_mock)
        driver.wait_for_element_to_disappear("some element", 1)

