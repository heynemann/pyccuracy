#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from pyccuracy import ActionRegistry, ActionBase
from pyccuracy.languages import LanguageItem

def test_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'I see "Welcome to Pyccuracy" title', 'en-us')
    assert issubclass(Action, ActionBase)
    assert isinstance(args, (list, tuple))
    assert isinstance(kw, dict)
    assert args[1] == u'Welcome to Pyccuracy'

def test_do_not_get_suitable_action():
    Action, args, kw = ActionRegistry.suitable_for(u'Blah bluh foo bar', 'en-us')
    assert Action is None
    assert args is None
    assert kw is None

def test_action_registry_suitable_for_returns_type_on_match():
    class FooTitleAction(ActionBase):
        regex = r'I see "foo" title'
        def execute(self, context, *args, **kwargs):
            pass

    Action, args, kwargs = ActionRegistry.suitable_for('I see "foo" title', 'en-us')
    assert isinstance(Action, type)
