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

cur_dir = abspath(dirname(os.curdir))
actions_dir = abspath(join(dirname(__file__), "../../pyccuracy/actions"))
languages_dir = abspath(join(dirname(__file__), "../../pyccuracy/languages"))

def test_settings_return_default_value_for_tests_dir():
    settings = Settings({})
    assert settings.tests_dirs == [cur_dir], "The tests dir should be %s but was %s." % (cur_dir, settings.tests_dir)

def test_settings_return_default_value_for_actions_dir():
    settings = Settings({})
    assert settings.actions_dir == actions_dir, "The actions_dir dir should be %s but was %s." % (actions_dir, settings.actions_dir)

def test_settings_return_default_value_for_languages_dir():
    settings = Settings({})
    assert settings.languages_dir == languages_dir, "The languages_dir dir should be %s but was %s." % (languages_dir, settings.languages_dir)

def test_settings_return_default_value_for_pages_dir():
    settings = Settings({})
    assert settings.pages_dir == [cur_dir], "The pages dir should be %s but was %s." % (cur_dir, settings.pages_dir)

def test_settings_return_default_value_for_custom_actions_dir():
    settings = Settings({})
    assert settings.custom_actions_dir == [cur_dir], "The custom actions dir should be %s but was %s." % (cur_dir, settings.custom_actions_dir)
