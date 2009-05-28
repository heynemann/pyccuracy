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

from pyccuracy.fixture import Fixture
from pyccuracy.pyccuracy_core import Settings
from pyccuracy.story_runner import StoryRunner

def test_story_runner_returns_a_result():
    settings = Settings()
    fixture = Fixture()
    runner = StoryRunner()

    result = runner.run_stories(settings, fixture)

    assert result is not None

def test_story_runner_returns_failed_story():
    settings = Settings()
    fixture = Fixture()
    runner = StoryRunner()

    result = runner.run_stories(settings, fixture)

    assert result is not None
