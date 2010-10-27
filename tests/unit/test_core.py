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
from mocker import Mocker, ANY, ARGS, KWARGS
from nose.tools import *

from pyccuracy.core import PyccuracyCore
from pyccuracy.common import Settings, Status
from pyccuracy.errors import TestFailedError

from utils import Object

def test_pyccuracy_core_instantiation():
    class MyParser:
        pass

    class MyRunner:
        pass

    pc = PyccuracyCore(MyParser(), MyRunner())
    assert isinstance(pc, PyccuracyCore)
    assert isinstance(pc.parser, MyParser)
    assert isinstance(pc.runner, MyRunner)

def make_context_and_fso_mocks(mocker):
    
    hooks_dir = ["/hooks/dir/"]
    pages_dir = ["/pages/dir/"]
    custom_actions_dir = ["/custom/actions/dir/"]
    
    context_mock = Object()
    context_mock.browser_driver = mocker.mock()
    context_mock.settings = mocker.mock()
    context_mock.settings.hooks_dir
    mocker.count(min=1, max=None)
    mocker.result(hooks_dir)
    context_mock.settings.pages_dir
    mocker.count(min=1, max=None)
    mocker.result(pages_dir)
    context_mock.settings.custom_actions_dir
    mocker.count(min=1, max=None)
    mocker.result(custom_actions_dir)
    context_mock.settings.base_url
    mocker.count(min=0, max=None)
    mocker.result("http://localhost")
    context_mock.settings.default_culture
    mocker.count(min=1, max=None)
    mocker.result("en-us")

    files = ["/some/weird/file.py"]
    fso_mock = mocker.mock()
    fso_mock.add_to_import(hooks_dir[0])
    fso_mock.add_to_import(pages_dir[0])
    fso_mock.add_to_import(custom_actions_dir[0])
    fso_mock.locate(hooks_dir[0], '*.py')
    mocker.result(files)
    fso_mock.locate(pages_dir[0], '*.py')
    mocker.result(files)
    fso_mock.locate(custom_actions_dir[0], '*.py')
    mocker.result(files)
    fso_mock.import_file(ANY)
    mocker.count(min=1, max=None)
    fso_mock.remove_from_import(custom_actions_dir[0])
    mocker.count(min=1, max=None)
    fso_mock.remove_from_import(pages_dir[0])
    mocker.count(min=1, max=None)
    fso_mock.remove_from_import(hooks_dir[0])
    mocker.count(min=1, max=None)

    return context_mock, fso_mock

def test_pyccuracy_core_run_tests():
    mocker = Mocker()
    context_mock, fso_mock = make_context_and_fso_mocks(mocker)
    context_mock.settings.write_report
    mocker.result(False)

    suite_mock = mocker.mock()
    suite_mock.no_story_header
    mocker.result([])
    suite_mock.stories
    mocker.result(['some story'])

    runner_mock = mocker.mock()
    parser_mock = mocker.mock()
    parser_mock.used_actions
    mocker.count(min=1, max=None)
    mocker.result([])
    
    results_mock = mocker.mock()
    results_mock.summary_for('en-us')
    mocker.result('my results')
    
    parser_mock.get_stories(ANY)
    mocker.result(suite_mock)
    runner_mock.run_stories(KWARGS)
    mocker.result(results_mock)
    
    with mocker:
        pc = PyccuracyCore(parser_mock, runner_mock)
    
        #TODO: falha
        results = pc.run_tests(should_throw=False, context=context_mock, fso=fso_mock)
        assert results == results_mock, results

def test_pyccuracy_core_run_tests_works_when_None_Result_returned_from_story_runner():
    
    mocker = Mocker()
    
    context_mock, fso_mock = make_context_and_fso_mocks(mocker)
    context_mock.settings.write_report
    mocker.result(False)
        
    suite_mock = mocker.mock()
    suite_mock.no_story_header
    mocker.result([])
    suite_mock.stories
    mocker.result(['some story'])

    runner_mock = mocker.mock()
    parser_mock = mocker.mock()
    parser_mock.used_actions
    mocker.count(min=1, max=None)
    mocker.result([])

    parser_mock.get_stories(ANY)
    mocker.result(suite_mock)
    runner_mock.run_stories(KWARGS)
    mocker.result(None)

    with mocker:
        pc = PyccuracyCore(parser_mock, runner_mock)
    
        assert pc.run_tests(should_throw=False, context=context_mock, fso=fso_mock) == None

def test_pyccuracy_core_should_raise_TestFailedError_when_should_throw_is_true():
    def do_run_tests_should_throw():
        
        mocker = Mocker()
        
        context_mock, fso_mock = make_context_and_fso_mocks(mocker)
        context_mock.settings.write_report
        mocker.result(False)

        context_mock.language = mocker.mock()
        context_mock.language.key
        mocker.result("key")

        results_mock = mocker.mock()
        results_mock.summary_for('en-us')
        mocker.result('')
        results_mock.get_status()
        mocker.result(Status.Failed)
        
        suite_mock = mocker.mock()
        suite_mock.no_story_header
        mocker.result([])
        suite_mock.stories
        mocker.result(['some story'])

        runner_mock = mocker.mock()
        parser_mock = mocker.mock()
        parser_mock.used_actions
        mocker.count(min=1, max=None)
        mocker.result([])
    
        parser_mock.get_stories(ANY)
        mocker.result(suite_mock)
        runner_mock.run_stories(KWARGS)
        mocker.result(results_mock)

        with mocker:
            pc = PyccuracyCore(parser_mock, runner_mock)
            pc.run_tests(should_throw=True, context=context_mock, fso=fso_mock)

    assert_raises(TestFailedError, do_run_tests_should_throw)

