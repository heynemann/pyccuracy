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

class TestFailedError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return unicode(self.message)

class ActionFailedError(Exception):
    def __unicode__(self):
        return self.message

class InvalidScenarioError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return unicode(self.message)

    def __unicode__(self):
        return self.message

class LanguageParseError(Exception):
    def __init__(self, culture, file_path, error_message = "The language file for %s could not be parsed at %s!"):
        self.culture = culture
        self.error_message = error_message
        self.file_path = file_path

    def __str__(self):
        return unicode(self.error_message) % (self.culture, self.file_path)

class SelectOptionError(Exception):
    def __init__(self, message):
        self.message = message
        print message

    def __str__(self):
        return unicode(self.message)

    def __unicode__(self):
        return self.message

class WrongArgumentsError(Exception):
    pass

class LanguageDoesNotResolveError(Exception):
    pass
