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

import re
import urllib2
import time

def force_unicode(s, encoding='utf-8', errors='strict'):
    if not isinstance(s, basestring,):
        if hasattr(s, '__unicode__'):
            s = unicode(s)
        else:
            try:
                s = unicode(str(s), encoding, errors)
            except UnicodeEncodeError:
                if not isinstance(s, Exception):
                    raise
                s = ' '.join([self.force_unicode(arg, encoding, errors) for arg in s])
    elif not isinstance(s, unicode):
        s = s.decode(encoding, errors)

    return s

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
