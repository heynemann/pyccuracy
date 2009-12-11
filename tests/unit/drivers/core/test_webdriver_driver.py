#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Licensed under the Open Software License ('OSL') v. 3.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyccuracy.drivers.core.webdriver_driver import WebDriverDriver

def test_check_css_style_is_visible():
    driver = WebDriverDriver(None)

    assert driver.check_css_style_is_visible('')
    assert not driver.check_css_style_is_visible('visibility: hidden;')
    assert not driver.check_css_style_is_visible('visibility : hidden')
    assert not driver.check_css_style_is_visible('display: none;')
    assert not driver.check_css_style_is_visible('display:none')
    assert not driver.check_css_style_is_visible('visibility: hidden; display: none;')
    assert not driver.check_css_style_is_visible('DISPLAY: NONE;')
