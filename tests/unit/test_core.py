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
from pmock import *
from nose.tools import *

from pyccuracy.core import PyccuracyCore
from pyccuracy.common import Settings, Status
from pyccuracy.errors import TestFailedError

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
    context_mock = Mock()
    context_mock.browser_driver = Mock()
    context_mock.settings = Mock()
    context_mock.settings.hooks_dir = ["/hooks/dir/"]
    context_mock.settings.pages_dir = ["/pages/dir/"]
    context_mock.settings.custom_actions_dir = ["/custom/actions/dir/"]
    context_mock.settings.base_url = "http://localhost"
    context_mock.settings.default_culture = "en-us"

    files = ["/some/weird/file.py"]
    actions  = ["/some/weird/action.py"]
    fso_mock = Mock()
    fso_mock.expects(once()).add_to_import(eq(context_mock.settings.hooks_dir[0]))
    fso_mock.expects(once()).add_to_import(eq(context_mock.settings.pages_dir[0]))
    fso_mock.expects(once()).add_to_import(eq(context_mock.settings.custom_actions_dir[0]))
    fso_mock.expects(once()).locate(eq(context_mock.settings.hooks_dir[0]), eq('*.py')).will(return_value(files))
    fso_mock.expects(once()).locate(eq(context_mock.settings.pages_dir[0]), eq('*.py')).will(return_value(files))
    fso_mock.expects(once()).locate(eq(context_mock.settings.custom_actions_dir[0]), eq('*.py')).will(return_value(files))
    fso_mock.expects(at_least_once()).method('import_file')
    fso_mock.expects(once()).remove_from_import(eq(context_mock.settings.custom_actions_dir[0]))
    fso_mock.expects(once()).remove_from_import(eq(context_mock.settings.pages_dir[0]))
    fso_mock.expects(once()).remove_from_import(eq(context_mock.settings.hooks_dir[0]))

    return context_mock, fso_mock

def test_pyccuracy_core_run_tests():
    context_mock, fso_mock = make_context_and_fso_mocks()
    context_mock.settings.write_report = False
    context_mock.language = Mock()
    context_mock.language.key = "pt-br"

    context_mock.browser_driver.expects(once()).method('start_test')
    context_mock.browser_driver.expects(once()).method('stop_test')

    results_mock = Mock()
    suite_mock = Mock()
    suite_mock.no_story_header = []

    runner_mock = Mock()
    parser_mock = Mock()
    parser_mock.used_actions = []
    parser_mock.expects(once()).method('get_stories').will(return_value(suite_mock))
    runner_mock.expects(once()).method('run_stories').will(return_value(results_mock))

    results_mock.expects(once()).summary_for(eq('en-us')).will(return_value('my results'))
    pc = PyccuracyCore(parser_mock, runner_mock)
    
    assert pc.run_tests(should_throw=False, context=context_mock, fso=fso_mock) == results_mock

    parser_mock.verify()
    runner_mock.verify()
    context_mock.verify()
    results_mock.verify()
    suite_mock.verify()
    fso_mock.verify()

def test_pyccuracy_core_run_tests_works_when_None_Result_returned_from_story_runner():
    context_mock, fso_mock = make_context_and_fso_mocks()
    context_mock.browser_driver.expects(once()).method('start_test')
    context_mock.browser_driver.expects(once()).method('stop_test')
    context_mock.language = Mock()
    context_mock.language.key = "pt-br"

    suite_mock = Mock()
    suite_mock.no_story_header = []

    runner_mock = Mock()
    parser_mock = Mock()
    parser_mock.used_actions = []
    parser_mock.expects(once()).method('get_stories').will(return_value(suite_mock))
    runner_mock.expects(once()).method('run_stories').will(return_value(None))

    pc = PyccuracyCore(parser_mock, runner_mock)

    assert pc.run_tests(should_throw=False, context=context_mock, fso=fso_mock) == None

    parser_mock.verify()
    runner_mock.verify()
    context_mock.verify()
    suite_mock.verify()
    fso_mock.verify()

def test_pyccuracy_core_should_raise_TestFailedError_when_should_throw_is_true():
    def do_run_tests_should_throw():
        context_mock, fso_mock = make_context_and_fso_mocks()
        context_mock.settings.write_report = False

        context_mock.browser_driver.expects(once()).method('start_test')
        context_mock.browser_driver.expects(once()).method('stop_test')
        context_mock.language = Mock()
        context_mock.language.key = "key"

        results_mock = Mock()
        suite_mock = Mock()
        suite_mock.no_story_header = []

        runner_mock = Mock()
        parser_mock = Mock()
        parser_mock.used_actions = []

        parser_mock.expects(once()).method('get_stories').will(return_value(suite_mock))
        runner_mock.expects(once()).method('run_stories').will(return_value(results_mock))

        results_mock.expects(once()).summary_for(eq('en-us')).will(return_value(''))
        results_mock.expects(once()).get_status().will(return_value(Status.Failed))
        pc = PyccuracyCore(parser_mock, runner_mock)
        pc.run_tests(should_throw=True, context=context_mock, fso=fso_mock)

        parser_mock.verify()
        runner_mock.verify()
        context_mock.verify()
        results_mock.verify()
        suite_mock.verify()
        fso_mock.verify()

    assert_raises(TestFailedError, do_run_tests_should_throw)

