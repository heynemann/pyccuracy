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
from pyccuracy.pyccuracy_core import PyccuracyCore, Settings
from mocker import Mocker

cur_dir = abspath(os.curdir)
actions_dir = abspath(join(dirname(__file__), "../../pyccuracy/actions"))
languages_dir = abspath(join(dirname(__file__), "../../pyccuracy/languages"))

def test_settings_return_default_value_for_tests_dir():
    settings = Settings({})
    assert settings.tests_dir == cur_dir, "The tests dir should be %s but was %s." % (cur_dir, settings.tests_dir)

def test_settings_return_default_value_for_actions_dir():
    settings = Settings({})
    assert settings.actions_dir == actions_dir, "The actions_dir dir should be %s but was %s." % (actions_dir, settings.actions_dir)

def test_settings_return_default_value_for_languages_dir():
    settings = Settings({})
    assert settings.languages_dir == languages_dir, "The languages_dir dir should be %s but was %s." % (languages_dir, settings.languages_dir)

def test_settings_return_default_value_for_pages_dir():
    pass

def test_settings_return_default_value_for_custom_actions_dir():
    pass

def test_settings_return_default_value_for_file_pattern():
    pass

def test_settings_return_default_value_for_scenarios_to_run():
    pass

def test_settings_return_default_value_for_default_culture():
    pass

def test_settings_return_default_value_for_base_url():
    pass

def test_settings_return_default_value_for_should_throw():
    pass

def test_settings_return_default_value_for_write_report():
    pass

def test_settings_return_default_value_for_report_file_dir():
    pass

def test_settings_return_default_value_for_report_file_name():
    pass

def test_settings_return_default_value_for_browser_to_run():
    pass

def test_settings_return_default_value_for_browser_driver():
    pass

def test_settings_return_default_value_for_extra_args():
    pass

#    mocker = Mocker()

#    mock_parser = mocker.mock()
#    
#    mocker.replay()

#    mock_runner = mocker.mock()
#    
#    mocker.replay()

#    core = PyccuracyCore(parser=mock_parser, runner=mock_runner)

#    result = core.run_tests()

#    assert result is not None, "The returned result cannot be none."
