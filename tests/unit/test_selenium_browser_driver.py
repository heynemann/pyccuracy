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

