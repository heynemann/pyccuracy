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
