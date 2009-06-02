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

DRIVERS = {}
from pyccuracy.drivers.interface import DriverInterface

class DriverRegistry(object):
    @classmethod
    def get(cls, name):
        Action = DRIVERS.get(name)

        if Action is None:
            raise DriverDoesNotExistError(name, 'Driver not found "%s". Is the driver in a known path?' % name)

        return Action

class MetaBaseDriver(type):
    def __init__(cls, name, bases, attrs):
        if name not in ('MetaBaseDriver', 'BaseDriver'):
            if not 'backend' in attrs.keys():
                raise BackendNotFoundError(name, 'Backend not found in "%s" class. Did you forget to specify "backend" attribute?' % name)

            DRIVERS[attrs['backend']] = cls

        super(MetaBaseDriver, cls).__init__(name, bases, attrs)

class BaseDriver(DriverInterface):
    __metaclass__ = MetaBaseDriver

    def __init__(self, settings):
        #Removed this to avoid circular reference
        #if not isinstance(settings, Settings):
        if not settings or settings.__class__.__name__ != "Settings":
            raise TypeError('%s takes a pyccuracy.common.Settings object as construction parameter. Got %s.' % (self.__class__.__name__, settings))

        self.settings = settings

    def start(self):
        pass

    def stop(self):
        pass

class DriverDoesNotExistError(Exception):
    def __init__(self, backend, msg):
        self._msg = msg
        self.backend = backend

    def __str__(self):
        return self._msg

class DriverError(Exception):
    pass

class BackendNotFoundError(Exception):
    def __init__(self, klass, msg):
        self._msg = msg
        self.klass = klass

    def __str__(self):
        return self._msg
