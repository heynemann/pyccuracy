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

from nose.tools import raises

from pyccuracy import ActionBase

def test_construction():
    class DoNothingAction(ActionBase):
        regex = r'^My Regex$'
        def execute(self, context, *args, **kwargs):
            pass

    assert DoNothingAction.regex == r'^My Regex$'

@raises(NotImplementedError)
def test_construction_fails_without_implementing_execute():
    class DoNothingAction(ActionBase):
        regex = r'^My Regex$'

@raises(NotImplementedError)
def test_construction_fails_without_implementing_setting_regex():
    class DoNothingAction(ActionBase):
        def execute(self, context, *args, **kw):
            pass

@raises(NotImplementedError)
def test_construction_fails_without_implementing_basic_attrs():
    class DoNothingAction(ActionBase):
        pass

@raises(TypeError)
def test_construction_fails_if_regex_nonstring():
    class DoNothingAction(ActionBase):
        regex = range(10)
        def execute(self, context, *args, **kw):
            pass

def test_can_resolve_string():
    class DoSomethingAction(ActionBase):
        regex = r'^(And )?I do "(?P<what>\w+)"$'
        def execute(self, context, *args, **kwargs):
            pass

    assert DoSomethingAction.can_resolve('And I do "test"')
    assert DoSomethingAction.can_resolve('I do "test"')

def test_cannot_resolve_string():
    class DoSomethingAction(ActionBase):
        regex = r'^(And )?I do "(?P<what>\w+)"$'
        def execute(self, context, *args, **kwargs):
            pass

    assert not DoSomethingAction.can_resolve('Not for me')
    assert not DoSomethingAction.can_resolve('Foo Bar')
