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

import operator

from pyccuracy.fixture_items import *
from pyccuracy.common import TimedItem, Status

class Fixture(TimedItem):
    def __init__(self):
        TimedItem.__init__(self)
        self.clear()

    def clear(self):
        self.invalid_test_files = []
        self.no_story_header = []
        self.stories = []

    def append_invalid_test_file(self, path, error):
        self.invalid_test_files.append((path, error))

    def append_no_story_header(self, path):
        self.no_story_header.append(path)

    def append_story(self, story):
        self.stories.append(story)
        return story

    def get_status(self):
        status = Status.Unknown
        for story in self.stories:
            if story.status == Status.Failed:
                return Status.Failed
            if story.status == Status.Successful:
                status = story.status
        return status

    def count_total_stories(self):
        return len(self.stories)

    def count_total_scenarios(self):
        return sum([len(story.scenarios) for story in self.stories])

    def count_successful_stories(self):
        return self.count_stories_by_status(Status.Successful)

    def count_failed_stories(self):
        return self.count_stories_by_status(Status.Failed)

    def count_stories_by_status(self, status):
        return len([story for story in self.stories if story.status == status])

    def count_successful_scenarios(self):
        return self.count_scenarios_by_status(Status.Successful)

    def count_failed_scenarios(self):
        return self.count_scenarios_by_status(Status.Failed)

    def count_scenarios_by_status(self, status):
        return len(self.get_scenarios_by_status(status))

    def get_successful_scenarios(self):
        return self.get_scenarios_by_status(Status.Successful)

    def get_failed_scenarios(self):
        return self.get_scenarios_by_status(Status.Failed)

    def get_scenarios_by_status(self, status):
        all_scenarios = []
        map(lambda item: all_scenarios.extend(item), [story.scenarios for story in self.stories])
        return [scenario for scenario in all_scenarios if scenario.status==status]

    def __str__(self):
        return self.get_results()
