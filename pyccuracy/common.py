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

import os
import re
import time
import fnmatch
import urllib2

from os.path import abspath, join, dirname

class URLChecker(object):
    """
    Taken from dead-parrot:

    http://github.com/gabrielfalcao/dead-parrot
    deadparrot/models/fields.py
    """

    def set_url(self, url):
        self.url = url

    def is_valid(self):
        url_regex = re.compile(r'^(https?|file):[/]{2}([\w_.-]+)+[.]\w{2,}([/]?.*)?')
        return url_regex.search(self.url) and True or False

    def does_exists(self):
        try:
            urllib2.urlopen(self.url)
            return True
        except urllib2.URLError:
            return False

class TimedItem(object):
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_run(self):
        '''Starts a run for this story. This method just keeps track of the time this story started.'''
        self.start_time = time.time()

    def end_run(self):
        '''Finishes a run for this story. This method just keeps track of the time this story finished.'''
        self.end_time = time.time()

    def ellapsed(self):
        '''The number of milliseconds that this story took to run.'''
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return 0
        return self.end_time - self.start_time

class Status:
    '''Possible statuses of a story, scenario or action.'''
    Unknown = "UNKNOWN"
    Failed = "FAILED"
    Successful = "SUCCESSFUL"

class StatusItem(object):
    def __init__(self, parent):
        self.status = Status.Unknown
        self.parent = parent
        self.error = None

    def mark_as_failed(self, error=None):
        '''Marks this story as failed.'''
        self.status = Status.Failed
        self.error = error
        if self.parent and isinstance(self.parent, StatusItem):
            self.parent.mark_as_failed()

    def mark_as_successful(self):
        '''Marks this story as successful only if it has not been marked failed before.'''
        if self.status != Status.Failed:
            self.status = Status.Successful
        if self.parent and isinstance(self.parent, StatusItem):
            self.parent.mark_as_successful()

class Settings(object):
    def __init__(self, settings=None):
        cur_dir = abspath(os.curdir)
        actions_dir = abspath(join(dirname(__file__), "actions"))
        languages_dir = abspath(join(dirname(__file__), "languages"))

        self.tests_dir = settings.get("tests_dir", cur_dir)

        self.actions_dir = settings.get("actions_dir", actions_dir)
        self.languages_dir = settings.get("languages_dir", languages_dir)

        self.pages_dir = settings.get("pages_dir", cur_dir)
        self.custom_actions_dir = settings.get("custom_actions_dir", cur_dir)

        self.file_pattern = settings.get("file_pattern", "*.acc")
        self.scenarios_to_run = settings.get("scenarios_to_run", None)
        self.default_culture = settings.get("default_culture", "en-us")
        self.base_url = settings.get("base_url", None)
        self.should_throw = settings.get("should_throw", False)
        self.write_report = settings.get("write_report", True)
        self.report_file_dir = settings.get("report_file_dir", cur_dir)
        self.report_file_name = settings.get("report_file_name", "report.html")
        self.browser_to_run = settings.get("browser_to_run", "chrome")
        self.browser_driver = settings.get("browser_driver", "selenium")
        self.extra_args = settings.get("extra_args", {})

class Context(object):
    def __init__(self, settings):
        self.settings = settings
        self.url = None
        self.current_page = None

def locate(pattern, root=os.curdir):
    root_path = os.path.abspath(root)
    for path, dirs, files in os.walk(root_path):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)
