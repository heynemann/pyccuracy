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

from utils import assert_raises
from pyccuracy.common import Settings
from pyccuracy.drivers import BaseDriver

def test_base_driver_instantiate_need_a_settings():
    def do_instantiate_fail():
        BaseDriver(None)

    assert_raises(TypeError, do_instantiate_fail, exc_pattern=re_compile('BaseDriver takes a pyccuracy.common.Settings object as construction parameter. Got None.'))

def test_base_driver_has_start_attr():
    assert hasattr(BaseDriver, 'start'), 'The BaseDriver should have the "start" attr'

def test_base_driver_start_attr_is_callable():
    assert callable(BaseDriver.start), 'The BaseDriver.start should be callable'

def test_base_driver_start_does_nothing():
    settings = Settings()
    assert BaseDriver(settings).start() is None

def test_base_driver_has_stop_attr():
    assert hasattr(BaseDriver, 'stop'), 'The BaseDriver should have the "stop" attr'

def test_base_driver_stop_attr_is_callable():
    assert callable(BaseDriver.stop), 'The BaseDriver.stop should be callable'

def test_base_driver_stop_does_nothing():
    settings = Settings()
    assert BaseDriver(settings).stop() is None
