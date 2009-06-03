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

from os.path import abspath, dirname, join
from pyccuracy.languages.templates import TemplateLoader
from pyccuracy.common import Status
from pyccuracy.airspeed import Template

class Result(object):
    def __init__(self, fixture, template_loader=None):
        self.fixture = fixture
        self.template_loader = template_loader

    def summary_for(self, language):
        template_string = self.get_summary_template_for(language)
        template = Template(template_string)
        return template.merge(self.summary_values())

    def get_summary_template_for(self, language):
        template_loader = self.template_loader or TemplateLoader(language)
        return template_loader.load("summary")

    def get_status(self):
        return self.fixture and self.fixture.get_status() or Status.Unknown

    def summary_values(self):
        val = {
                "run_status" : Status.Unknown,
                "total_stories" : 0,
                "total_scenarios" : 0,
                "successful_stories" : 0,
                "failed_stories" : 0,
                "successful_scenarios" : 0,
                "failed_scenarios" : 0,
                "has_failed_scenarios": False,
                "threshold":"0.00"
              }

        if self.fixture:
            val = {
                    "run_status" : self.fixture.get_status(),
                    "total_stories" : self.fixture.count_total_stories(),
                    "total_scenarios" : self.fixture.count_total_scenarios(),
                    "successful_stories" : self.fixture.count_successful_stories(),
                    "failed_stories" : self.fixture.count_failed_stories(),
                    "successful_scenarios" : self.fixture.count_successful_scenarios(),
                    "failed_scenarios" : self.fixture.count_failed_scenarios()
                  }
            total_test_time = float(self.fixture.ellapsed())
            if total_test_time == 0:
                val["threshold"] = 0
            else:
                val["threshold"] = "%.2f" % (val["total_scenarios"] / (total_test_time / 60))

            val["has_failed_scenarios"] = val["failed_scenarios"] > 0

        if val["has_failed_scenarios"]:
            val["failed_scenario_instances"] = self.fixture.get_failed_scenarios()

        no_stories = val["total_stories"] == 0
        no_scenarios = val["total_scenarios"] == 0

        val["successful_story_percentage"] = no_stories and "0.00" or "%.2f" % (float(val["successful_stories"]) / float(val["total_stories"]) * 100)
        val["failed_story_percentage"] = no_stories and "0.00" or "%.2f" % (float(val["failed_stories"]) / float(val["total_stories"]) * 100)
        val["successful_scenario_percentage"] = no_scenarios and "0.00" or "%.2f" % (float(val["successful_scenarios"]) / float(val["total_scenarios"]) * 100)
        val["failed_scenario_percentage"] = no_scenarios and "0.00" or "%.2f" % (float(val["failed_scenarios"]) / float(val["total_scenarios"]) * 100)

        if self.fixture.no_story_header:
            val["has_no_header_files"] = True
            val["no_header_files"] = self.fixture.no_story_header

        val["test_run_seconds"] = "%.2f" % total_test_time

        return val

    @classmethod
    def empty(cls):
        return Result(fixture=None)
