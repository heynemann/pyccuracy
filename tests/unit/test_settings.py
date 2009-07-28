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
from pyccuracy.common import Settings

def test_settings_return_default_value_for_tests_dirs():
    settings = Settings({}, cur_dir='/root')
    assert settings.tests_dirs[0] == '/root', "The tests dir should be %s but was %s." % ('/root', settings.tests_dirs[0])

def test_settings_return_default_value_for_actions_dir():
    settings = Settings({}, actions_dir='/actions')
    assert settings.actions_dir == '/actions', "The actions_dir dir should be %s but was %s." % ('/actions', settings.actions_dir)

def test_settings_return_default_value_for_languages_dir():
    settings = Settings({}, languages_dir)
    assert settings.languages_dir == '/languages', "The languages_dir dir should be %s but was %s." % ('/languages', settings.languages_dir)

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
    assert settings.scenarios_to_run == [], "The scenarios to run should be None but was %s." % (settings.scenarios_to_run)

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

#Specified Values
def test_settings_return_custom_value_for_tests_dirs():
    settings = Settings({"tests_dirs":["a","b"]})
    expected = [abspath("a"), abspath("b")]
    assert settings.tests_dirs == expected, "The tests dir should be %s but was %s." % (expected, settings.tests_dirs)

def test_settings_return_default_value_for_actions_dir():
    settings = Settings({"actions_dir":"a"})
    assert settings.actions_dir == "a", "The actions_dir dir should be %s but was %s." % ("a", settings.actions_dir)

def test_settings_return_default_value_for_languages_dir():
    settings = Settings({"languages_dir":"a"})
    assert settings.languages_dir == "a", "The languages_dir dir should be %s but was %s." % ("a", settings.languages_dir)

def test_settings_return_default_value_for_pages_dir():
    settings = Settings({"pages_dir":"a"})
    assert settings.pages_dir == "a", "The pages dir should be %s but was %s." % ("a", settings.pages_dir)

def test_settings_return_default_value_for_custom_actions_dir():
    settings = Settings({"custom_actions_dir":"a"})
    assert settings.custom_actions_dir == "a", "The custom actions dir should be %s but was %s." % ("a", settings.custom_actions_dir)

def test_settings_return_default_value_for_file_pattern():
    settings = Settings({"file_pattern":"a"})
    assert settings.file_pattern == "a", "The pattern should be a but was %s." % (settings.file_pattern)

def test_settings_return_default_value_for_scenarios_to_run():
    settings = Settings({"scenarios_to_run":"a"})
    assert settings.scenarios_to_run == ["a"], "The scenarios to run should be 'a' but was %s." % (settings.scenarios_to_run)

def test_settings_return_default_value_for_default_culture():
    settings = Settings({"default_culture":"a"})
    assert settings.default_culture == "a", "The default culture should be 'a' but was %s." % (settings.default_culture)

def test_settings_return_default_value_for_base_url():
    settings = Settings({"base_url":"a"})
    assert settings.base_url == "a", "The base url should be 'a' but was %s." % (settings.base_url)

def test_settings_return_default_value_for_should_throw():
    settings = Settings({"should_throw":True})
    assert settings.should_throw, "The should_throw setting should be True but was %s." % (settings.should_throw)

def test_settings_return_default_value_for_write_report():
    settings = Settings({"write_report":False})
    assert not settings.write_report, "The write_report setting should be False but was %s." % (settings.write_report)

def test_settings_return_default_value_for_report_file_dir():
    settings = Settings({"report_file_dir":"a"})
    assert settings.report_file_dir == "a", "The report_file_dir should be %s but was %s." % ("a", settings.report_file_dir)

def test_settings_return_default_value_for_report_file_name():
    settings = Settings({"report_file_name":"a"})
    assert settings.report_file_name == "a", "The report_file_name should be 'a' but was %s." % (settings.report_file_name)

def test_settings_return_default_value_for_browser_to_run():
    settings = Settings({"browser_to_run":"a"})
    assert settings.browser_to_run == "a", "The browser_to_run should be 'a' but was %s." % (settings.browser_to_run)

def test_settings_return_default_value_for_browser_driver():
    settings = Settings({"browser_driver":"a"})
    assert settings.browser_driver == "a", "The browser_driver should be 'a' but was %s." % (settings.browser_driver)

def test_settings_return_default_value_for_extra_args():
    d = {"a":"b"}
    settings = Settings({"extra_args":d})
    assert settings.extra_args == {"a":"b"}, "The extra_args should be an %s but was %s." % (d, settings.extra_args)
