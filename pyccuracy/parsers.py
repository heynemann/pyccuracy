#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

import re
import os

from pyccuracy import ActionRegistry
from pyccuracy.actions import ActionNotFoundError
from pyccuracy.languages import LanguageGetter
from pyccuracy.common import locate
from pyccuracy.fixture import Fixture
from pyccuracy.fixture_items import Story, Action, Scenario

class FSO(object):
    '''Actual Filesystem'''
    def list_files(self, directories, pattern):
        files = []
        for directory in directories:
            files.extend(locate(root=directory, pattern=pattern))
        return files

    def read_file(self, file_path):
        return open(file_path).read().decode('utf-8')

class FileParser(object):
    def __init__(self, language=None, file_object=None, action_registry=None):
        self.file_object = file_object and file_object or FSO()
        self.action_registry = action_registry and action_registry or ActionRegistry
        self.language = language
        self.used_actions = []

    def get_stories(self, settings):
        if not self.language:
            self.language = LanguageGetter(settings.default_culture)

        fixture = Fixture()

        story_file_list = self.file_object.list_files(directories=settings.tests_dirs, pattern=settings.file_pattern)
        story_file_list.sort()

        for story_file_path in story_file_list:
            try:
                parsed, error, story = self.parse_story_file(story_file_path, settings)
                if parsed:
                    fixture.append_story(story)
                else:
                    fixture.append_no_story_header(story_file_path)
            except IOError, err:
                fixture.append_invalid_test_file(story_file_path, err)
            except ValueError, verr:
                fixture.append_no_story_header(story_file_path)
        return fixture

    def parse_story_file(self, story_file_path, settings):
        story_text = self.file_object.read_file(story_file_path)
        story_lines = [line.strip() for line in story_text.splitlines() if line.strip() != ""]

        headers = self.assert_header(story_lines, settings.default_culture)
        if not headers:
            return (False, self.language.get('no_header_failure'), None)

        as_a = headers[0]
        i_want_to = headers[1]
        so_that = headers[2]

        current_story = Story(as_a=as_a, i_want_to=i_want_to, so_that=so_that, identity=story_file_path)

        scenario_lines = story_lines[3:]

        current_scenario = None
        for line in scenario_lines:
            if self.is_scenario_starter_line(line):
                current_scenario = self.parse_scenario_line(current_story, line, settings)
                continue

            if self.is_keyword(line, "given"):
                current_area = "given"
                continue
            if self.is_keyword(line, "when"):
                current_area = "when"
                continue
            if self.is_keyword(line, "then"):
                current_area = "then"
                continue

            if current_scenario is None:
                if settings.scenarios_to_run:
                    continue
                else:
                    raise ValueError("No scenario line found before first action.")

            add_method = getattr(current_scenario, "add_%s" % current_area)

            if line.startswith("#"):
                add_method(line, lambda context, *args, **kwargs: None, [], {})
                continue

            action, args, kwargs = self.action_registry.suitable_for(line, settings.default_culture)

            if not action:
                self.raise_action_not_found_for_line(line, current_scenario, story_file_path)
            
            if not action in self.used_actions:
                self.used_actions.append(action)

            instance = action()
            if kwargs:
                args = []
            add_method(line, instance.execute, args, kwargs)

        return (True, None, current_story)

    def assert_header(self, story_lines, culture):
        as_a = self.language.get('as_a')
        i_want_to = self.language.get('i_want_to')
        so_that = self.language.get('so_that')

        if len(story_lines) < 3:
            return []

        if not as_a in story_lines[0] \
           or not i_want_to in story_lines[1] \
           or not so_that in story_lines[2]:
            return []

        return [story_lines[0].replace(as_a, "").strip(),
                 story_lines[1].replace(i_want_to, "").strip(),
                 story_lines[2].replace(so_that, "").strip()]

    def is_scenario_starter_line(self, line):
        scenario_keyword = self.language.get('scenario')
        return line.strip().startswith(scenario_keyword)

    def is_keyword(self, line, keyword):
        keyword = self.language.get(keyword)
        return line.strip() == keyword

    def parse_scenario_line(self, current_story, line, settings):
        scenario_keyword = self.language.get('scenario')
        scenario_values = line.split(u'-')
        index = scenario_values[0].replace(scenario_keyword,"").strip()
        title = scenario_values[1].strip()
        current_scenario = None
        if not settings.scenarios_to_run or index in settings.scenarios_to_run:
            current_scenario = current_story.append_scenario(index, title)
        return current_scenario

    def raise_action_not_found_for_line(self, line, scenario, filename):
        raise ActionNotFoundError(line, scenario, filename)
