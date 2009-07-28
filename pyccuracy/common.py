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
from glob import glob

from os.path import abspath, join, dirname, exists

from pyccuracy.languages import *
from pyccuracy.drivers import *
from pyccuracy.actions import ActionRegistry

def get_curdir():
    return abspath(dirname(os.curdir))

class URLChecker(object):
    """
    Taken from dead-parrot:

    http://github.com/gabrielfalcao/dead-parrot
    deadparrot/models/fields.py
    """

    def __init__(self, lib=urllib2):
        self.lib = lib

    def set_url(self, url):
        self.url = url

    def is_valid(self):
        url_regex = re.compile(r'^(https?|file):[/]{2}([\w_.-]+)+[.]?\w{2,}([:]\d+)?([/]?.*)?')
        return url_regex.search(self.url) and True or False

    def exists(self):
        try:
            self.lib.urlopen(self.url)
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
            return time.time() - self.start_time

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
    def __init__(self,
                 settings=None,
                 cur_dir=get_curdir(),
                 actions_dir=None,
                 abspath_func=abspath,
                 languages_dir=None):

        if not settings:
            settings = {}

        if not actions_dir:
            actions_dir = abspath_func(join(dirname(__file__), "actions"))

        if not languages_dir:
            languages_dir = abspath_func(join(dirname(__file__), "languages"))

        self.tests_dirs = [abspath_func(test_dir) for test_dir in self.get_setting(settings, "tests_dirs", [cur_dir])]

        self.actions_dir = self.get_setting(settings, "actions_dir", actions_dir)
        self.languages_dir = self.get_setting(settings, "languages_dir", languages_dir)

        self.pages_dir = self.get_setting(settings, "pages_dir", self.tests_dirs)
        if not self.pages_dir:
            self.pages_dir = self.tests_dirs
        self.custom_actions_dir = self.get_setting(settings, "custom_actions_dir", self.tests_dirs)
        if not self.custom_actions_dir:
            self.custom_actions_dir = self.tests_dirs

        self.file_pattern = self.get_setting(settings, "file_pattern", "*.acc")
        self.scenarios_to_run = self.get_setting(settings, "scenarios_to_run", [])
        if self.scenarios_to_run:
            self.scenarios_to_run = self.scenarios_to_run.replace(" ","").split(",")

        self.default_culture = self.get_setting(settings, "default_culture", "en-us")
        self.base_url = self.get_setting(settings, "base_url", None)
        self.should_throw = self.get_setting(settings, "should_throw", False)
        self.write_report = self.get_setting(settings, "write_report", True)
        self.report_file_dir = self.get_setting(settings, "report_file_dir", cur_dir)
        self.report_file_name = self.get_setting(settings, "report_file_name", "report.html")
        self.browser_to_run = self.get_setting(settings, "browser_to_run", "chrome")
        self.browser_driver = self.get_setting(settings, "browser_driver", "selenium")
        self.worker_threads = int(self.get_setting(settings, "workers", 1))
        self.extra_args = self.get_setting(settings, "extra_args", {})
        self.on_scenario_started = self.get_setting(settings, "on_scenario_started", None)
        self.on_scenario_completed = self.get_setting(settings, "on_scenario_completed", None)

    def get_setting(self, settings, key, default):
        value = settings.get(key, None)

        if value is None:
            return default

        return value

class Context(object):
    def __init__(self, settings):
        self.settings = settings
        self.language = AVAILABLE_GETTERS[settings.default_culture]
        self.browser_driver = DriverRegistry.get(settings.browser_driver)(self)
        self.url = None
        self.current_page = None

def locate(pattern, root=os.curdir, recursive=True):
    root_path = os.path.abspath(root)

    if recursive:
        return_files = []
        for path, dirs, files in os.walk(root_path):
            for filename in fnmatch.filter(files, pattern):
                return_files.append(os.path.join(path, filename))
        return return_files
    else:
        return glob(join(root_path, pattern))
