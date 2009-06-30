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

import re

from pyccuracy.errors import ActionFailedError, LanguageDoesNotResolveError
from pyccuracy.languages import LanguageItem, AVAILABLE_GETTERS, LanguageGetter

ACTIONS = []

class ActionNotFoundError(Exception):
    def __init__(self, line, scenario, filename):
        self.line = line
        self.scenario = scenario
        self.filename = filename

    def __str__(self):
        return unicode(self)
    def __unicode__(self):
        return "Action Not Found: %s\nScenario: %s\nFilename: %s" % (self.line, self.scenario, self.filename)

class ActionRegistry(object):
    @classmethod
    def suitable_for(cls, line, language, getter=None):
        getter = getter or AVAILABLE_GETTERS[language]

        for Action in ACTIONS:
            regex = Action.regex

            if isinstance(regex, (basestring, LanguageItem)):
                if isinstance(Action.regex, LanguageItem):
                    regex = getter.get(Action.regex)
                    if regex is None:
                        raise LanguageDoesNotResolveError('The language "%s" does not resolve the string "%s"' % (language, Action.regex))

                supported_elements = getter.get("supported_elements")
                regex = regex.replace("<element selector>", supported_elements)

                Action.regex = re.compile(regex)

            matches = Action.regex.match(line)

            if matches:
                args = matches.groups()
                kw = matches.groupdict()
                for k, v in kw.items():
                    del kw[k]
                    kw[str(k)] = v
                return Action, args, kw

        return None, None, None

class MetaActionBase(type):
    def __init__(cls, name, bases, attrs):
        if name not in ('ActionBase', ):
            if 'execute' not in attrs:
                raise NotImplementedError("The action %s does not implements the method execute()" % name)
            if 'regex' not in attrs:
                raise NotImplementedError("The action %s does not implements the attribute regex" % name)

            if not isinstance(attrs['regex'], basestring):
                regex = attrs['regex']
                raise TypeError("%s.regex attribute must be a string, got %r(%r)." % (regex.__class__, regex))

            # registering
            ACTIONS.append(cls)

        super(MetaActionBase, cls).__init__(name, bases, attrs)

class ActionBase(object):
    __metaclass__ = MetaActionBase
    failed = ActionFailedError

    @classmethod
    def can_resolve(cls, string):
        return re.match(cls.regex, string)

    def execute_action(self, line, context, getter=None):
        # the getter is here for unit testing reasons
        Action, args, kwargs = ActionRegistry.suitable_for(line, context.settings.default_culture, getter=getter)

        if not Action:
            raise ActionNotFoundError(line, None, None)

        if isinstance(self, Action):
            raise RuntimeError('A action can not execute itself for infinite recursion reasons :)')

        action_to_execute = Action()
        if kwargs:
            args = []
        action_to_execute.execute(context, *args, **kwargs)

    def resolve_element_key(self, context, element_type, element_key):
        page = context.current_page

        resolved_element = None

        if page:
            resolved_element = page.get_registered_element(element_key)

        if not resolved_element:
            resolved_element = context.browser_driver.resolve_element_key(context, element_type, element_key)

        if not resolved_element:
            raise KeyError("No element could be resolved for element type %s and element key %s" % (element_type, element_key))

        return resolved_element

    def is_element_visible(self, context, selector):
        is_visible = context.browser_driver.is_element_visible(selector)
        return is_visible

    def assert_element_is_visible(self, context, selector, message):
        if not self.is_element_visible(context, selector):
            raise self.failed(message + "(Resolved to Element %s)" % selector)

    def assert_element_is_not_visible(self, context, selector, message):
        if self.is_element_visible(context, selector):
            raise self.failed(message + "(Resolved to Element %s)" % selector)

