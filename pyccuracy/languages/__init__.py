# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from os import listdir
from os.path import abspath, dirname, join

AVAILABLE_LANGUAGES = [l.replace('.txt', '') for l in listdir(join(abspath(dirname(__file__)), 'data'))]

class LanguageGetter(object):
    def __init__(self, language, file_object=None):
        if not isinstance(language, basestring):
            error = 'LanguageGetter takes a string as construction ' \
                    'parameter, got %r(%r)'
            raise TypeError(error % (language.__class__, language))

        self.curdir = abspath(dirname(__file__))
        self.language_path = join(self.curdir, 'data', '%s.txt' % language)
        self.raw_data = None
        self.file_object = file_object
        self.data = {}

    def fill_data(self):
        if not self.file_object:
            self.file_object = open(self.language_path)

        self.raw_data = self.file_object.read()
        for line in self.raw_data.split('\n'):
            if '=' not in line:
                continue

            k, v = line.split('=')
            self.data[k.strip()] = unicode(v.strip())

    def get(self, key):
        if not self.data:
            self.fill_data()

        return self.data.get(key)

class LanguageItem(unicode):
    pass
