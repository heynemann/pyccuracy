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

import os
from os.path import join, abspath, dirname

import fudge
from nose.tools import *

from pyccuracy.core import PyccuracyCore
from pyccuracy.common import Settings, Status
from pyccuracy.errors import TestFailedError
from pyccuracy.result import Result

class Object(object):
    pass

def teardown():
    fudge.clear_expectations()

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_pyccuracy_core_instantiation():
    class MyParser:
        pass

    class MyRunner:
        pass

    pc = PyccuracyCore(MyParser(), MyRunner())
    assert isinstance(pc, PyccuracyCore)
    assert isinstance(pc.parser, MyParser)
    assert isinstance(pc.runner, MyRunner)

def make_context_and_fso_mocks():
    context_mock = Object()
    context_mock.browser_driver = fudge.Fake('browser_driver')
    context_mock.settings = Object()
    context_mock.settings.hooks_dir = ["/hooks/dir/"]
    context_mock.settings.pages_dir = ["/pages/dir/"]
    context_mock.settings.custom_actions_dir = ["/custom/actions/dir/"]
    context_mock.settings.base_url = "http://localhost"
    context_mock.settings.default_culture = "en-us"

    files = ["/some/weird/file.py"]
    actions  = ["/some/weird/action.py"]
    fso_mock = fudge.Fake('fso_mock')
    
    fso_mock.expects('add_to_import').with_args(context_mock.settings.hooks_dir[0])
    fso_mock.expects('add_to_import').with_args(context_mock.settings.pages_dir[0])
    fso_mock.expects('add_to_import').with_args(context_mock.settings.custom_actions_dir[0])
    
    fso_mock.expects('locate').with_args(context_mock.settings.hooks_dir[0], '*.py').returns(files)
    fso_mock.expects('locate').with_args(context_mock.settings.pages_dir[0], '*.py').returns(files)
    fso_mock.expects('locate').with_args(context_mock.settings.custom_actions_dir[0], '*.py').returns(files)
    
    fso_mock.expects('import_file')
    
    fso_mock.expects('remove_from_import').with_args(context_mock.settings.hooks_dir[0])
    fso_mock.expects('remove_from_import').with_args(context_mock.settings.pages_dir[0])
    fso_mock.expects('remove_from_import').with_args(context_mock.settings.custom_actions_dir[0])

    return context_mock, fso_mock

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_pyccuracy_core_run_tests():
    context_mock, fso_mock = make_context_and_fso_mocks()
    context_mock.settings.write_report = False
    context_mock.language = Object()
    context_mock.language.key = "pt-br"

    results_mock = fudge.Fake('results_mock')
    results_mock.expects('summary_for').with_args('en-us').returns('my results')
    suite_mock = fudge.Fake('suite_mock').has_attr(no_story_header=[], stories=['some story'])

    runner_mock = fudge.Fake('runner_mock')
    parser_mock = fudge.Fake('parser_mock').has_attr(used_actions=[])
    parser_mock.expects('get_stories').returns(suite_mock)
    runner_mock.expects('run_stories').returns(results_mock)
    
    with fudge.patched_context(Result, 'summary_for', lambda: 'my results'):
        pc = PyccuracyCore(parser_mock, runner_mock)
        
        result = pc.run_tests(should_throw=False, context=context_mock, fso=fso_mock)
        assert result.summary_for('en-us') == 'my results'

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_pyccuracy_core_run_tests_works_when_None_Result_returned_from_story_runner():
    context_mock, fso_mock = make_context_and_fso_mocks()
    context_mock.settings.write_report = False
    
    context_mock.language = Object()
    context_mock.language.key = "pt-br"

    suite_mock = fudge.Fake('suite_mock').has_attr(no_story_header=[], stories=['some story'])

    runner_mock = fudge.Fake('runner_mock')
    parser_mock = fudge.Fake('parser_mock').has_attr(used_actions=[])
    parser_mock.expects('get_stories').returns(suite_mock)
    runner_mock.expects('run_stories').returns(None)

    pc = PyccuracyCore(parser_mock, runner_mock)

    assert pc.run_tests(should_throw=False, context=context_mock, fso=fso_mock) == None

@with_setup(teardown=teardown)
@fudge.with_fakes
def test_pyccuracy_core_should_raise_TestFailedError_when_should_throw_is_true():
    def do_run_tests_should_throw():
        context_mock, fso_mock = make_context_and_fso_mocks()
        context_mock.settings.write_report = False
        
        context_mock.language = Object()
        context_mock.language.key = "key"

        results_mock = fudge.Fake('results_mock')
        results_mock.expects('summary_for').with_args('en-us').returns('')
        results_mock.expects('get_status').returns(Status.Failed)
        suite_mock = fudge.Fake('suite_mock').has_attr(no_story_header=[], stories=['some story'])

        runner_mock = fudge.Fake()
        parser_mock = fudge.Fake('parser_mock').has_attr(used_actions=[])

        parser_mock.expects('get_stories').returns(suite_mock)
        runner_mock.expects('run_stories').returns(results_mock)

        pc = PyccuracyCore(parser_mock, runner_mock)
        pc.run_tests(should_throw=True, context=context_mock, fso=fso_mock)

    assert_raises(TestFailedError, do_run_tests_should_throw)

