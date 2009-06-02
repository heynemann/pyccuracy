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
from nose.tools import *

from utils import assert_raises
from pyccuracy import DriverRegistry
from pyccuracy.drivers import BaseDriver, DriverDoesNotExistError, BackendNotFoundError

def test_drivers_registry_must_raise_when_does_not_exist():
    def do_get_must_fail():
        null_driver = DriverRegistry.get('spam_eggs')

    assert_raises(DriverDoesNotExistError, do_get_must_fail, exc_pattern=re_compile(u'^Driver not found "spam_eggs". Is the driver in a known path[?]$'))
    # maybe we should rename the exception to "NeedAGpsError" ? LOL

def test_drivers_registry_exception_must_have_backend_attribute():
    def do_get_must_fail():
        null_driver = DriverRegistry.get('spam_eggs')

    try:
        do_get_must_fail()
        assert False, "If you got here, something's amiss"

    except DriverDoesNotExistError, e:
        assert hasattr(e, 'backend')
        assert e.backend == 'spam_eggs'

def test_drivers_registry_get_custom_browser():
    class MyBrowserDriver1(BaseDriver):
        backend = 'my_backend'

    Driver = DriverRegistry.get('my_backend')
    assert Driver is MyBrowserDriver1

def test_drivers_registry_should_raise_when_no_backend_specified():
    def raise_my_stuff():
        class MyBrowserDriver2(BaseDriver):
            pass

    assert_raises(BackendNotFoundError, raise_my_stuff, exc_pattern=re_compile('^Backend not found in "MyBrowserDriver2" class. Did you forget to specify "backend" attribute[?]$'))

def test_drivers_registry_should_raise_and_exception_must_have_klass_attribute():
    def raise_my_stuff():
        class MyBrowserDriver3(BaseDriver):
            pass
    try:
        raise_my_stuff()
        assert False, "If you got here, something's amiss"

    except BackendNotFoundError, e:
        assert hasattr(e, 'klass')
        assert e.klass == 'MyBrowserDriver3'
