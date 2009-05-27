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
    settings = Settings({})
    assert settings.pages_dir == cur_dir, "The pages dir should be %s but was %s." % (cur_dir, settings.pages_dir)

def test_settings_return_default_value_for_custom_actions_dir():
    settings = Settings({})
    assert settings.custom_actions_dir == cur_dir, "The custom actions dir should be %s but was %s." % (cur_dir, settings.custom_actions_dir)

def test_settings_return_default_value_for_file_pattern():
    settings = Settings({})
    assert settings.file_pattern == "*.acc", "The pattern should be *.acc but was %s." % (settings.file_pattern)

def test_settings_return_default_value_for_scenarios_to_run():
    settings = Settings({})
    assert settings.scenarios_to_run is None, "The scenarios to run should be None but was %s." % (settings.scenarios_to_run)

def test_settings_return_default_value_for_default_culture():
    settings = Settings({})
    assert settings.default_culture == "en-us", "The default culture should be en-us but was %s." % (settings.default_culture)

def test_settings_return_default_value_for_base_url():
    settings = Settings({})
    assert settings.base_url is None, "The base url should be None but was %s." % (settings.base_url)

def test_settings_return_default_value_for_should_throw():
    settings = Settings({})
    assert not settings.should_throw, "The should_throw setting should be False but was %s." % (settings.should_throw)

def test_settings_return_default_value_for_write_report():
    settings = Settings({})
    assert settings.write_report, "The write_report setting should be True but was %s." % (settings.write_report)

def test_settings_return_default_value_for_report_file_dir():
    settings = Settings({})
    assert settings.report_file_dir == cur_dir, "The report_file_dir should be %s but was %s." % (cur_dir, settings.report_file_dir)

def test_settings_return_default_value_for_report_file_name():
    settings = Settings({})
    assert settings.report_file_name == "report.html", "The report_file_name should be report.html but was %s." % (settings.report_file_name)

def test_settings_return_default_value_for_browser_to_run():
    settings = Settings({})
    assert settings.browser_to_run == "chrome", "The browser_to_run should be chrome but was %s." % (settings.browser_to_run)

def test_settings_return_default_value_for_browser_driver():
    settings = Settings({})
    assert settings.browser_driver == "selenium", "The browser_driver should be selenium but was %s." % (settings.browser_driver)

def test_settings_return_default_value_for_extra_args():
    settings = Settings({})
    assert settings.extra_args == {}, "The extra_args should be an empty dict but was %s." % (settings.extra_args)

