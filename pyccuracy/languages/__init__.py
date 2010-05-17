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

import codecs
from os import listdir
from os.path import abspath, dirname, join

from pyccuracy.errors import WrongArgumentsError

AVAILABLE_LANGUAGES = [l.replace('.txt', '') for l in listdir(join(abspath(dirname(__file__)), 'data')) if l.endswith('txt')]

class Singleton(object):
    __SINGLETON_INSTANCES__ = {}
    def __new__(cls, *args, **kw):
        key = cls.__name__, args, tuple(kw.values())
        if key not in cls.__SINGLETON_INSTANCES__.keys():
            cls.__SINGLETON_INSTANCES__[key] = super(type, cls).__new__(cls)
 
        return cls.__SINGLETON_INSTANCES__[key]

class LanguageGetter(Singleton):
    def __init__(self, language, file_object=None):
        if not isinstance(language, basestring):
            error = 'LanguageGetter takes a string as construction ' \
                    'parameter, got %r(%r)'
            raise TypeError(error % (language.__class__, language))

        self.key = language
        self.curdir = abspath(dirname(__file__))
        self.language_path = join(self.curdir, 'data', '%s.txt' % language)
        self.raw_data = None
        self.file_object = file_object
        self.data = {}

    def fill_data(self):
        if not self.file_object:
            self.file_object = codecs.open(self.language_path, "r", "utf-8")

        self.raw_data = self.file_object.read()
        for line in self.raw_data.split('\n'):
            if '=' not in line:
                continue

            values = line.split('=')
            k = values[0]
            v = "=".join(values[1:])
            self.data[k.strip()] = unicode(v.strip())

    def get(self, key):
        if not self.data:
            self.fill_data()

        return self.data.get(key)

    def format(self, string, *args, **kwargs):
        resolved_string = self.get(string)
        need_kwargs = bool(len(resolved_string.split("%(")) > 1)

        try:
            if need_kwargs:
                return resolved_string % kwargs
            else:
                return resolved_string % args

        except ValueError, e:
            total_args = len(resolved_string.split('%'))
            total_got_args = len(args)
            raise WrongArgumentsError('The resolved_string "%s" gets exactly %d args, got %d' % (resolved_string, total_args, total_got_args))

        except TypeError, e:
            raise WrongArgumentsError('The resolved_string "%s" gets is formatted through *args, but got **kwargs' % resolved_string)

        except KeyError, e:
            raise WrongArgumentsError('The resolved_string "%s" gets is formatted through **kwargs, but got *args' % resolved_string)


class LanguageItem(unicode):
    pass

AVAILABLE_GETTERS = dict([(language, LanguageGetter(language)) for language in AVAILABLE_LANGUAGES])
