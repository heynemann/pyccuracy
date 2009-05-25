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

from errors import *
from common import force_unicode
import os
import re

class Language(object):
    def __init__(self, languages_dir):
        self.__clear()
        self.languages_dir = languages_dir

    def __clear(self):
        self.language_items = {}

    def load(self, culture):
        self.__clear()
        file_name = "language_" + culture + ".txt"
        file_path = os.path.join(self.languages_dir, file_name)

        if not os.path.exists(file_path):
            raise LanguageParseError(culture, file_path)

        try:
            content = unicode(open(file_path).read(), encoding='utf-8')
            lines = [line.strip() for line in content.split("\n") if len(line)]
        except ValueError:
            raise LanguageParseError(culture, file_path)

        for line in [line for line in lines if not line.startswith("#")]:
            key, value = line.split("=")
            key = key.strip()
            value = force_unicode(value.strip())

            if "<element selector>" in value:
                value = value.replace("<element selector>", self.language_items["supported_elements"])

            if key.endswith("_regex"):
                value = re.compile(value, re.U)
            self.language_items[key.strip()] = value

    def __getitem__(self, key):
        item = self.language_items.get(key, None)
        if item is None: 
            raise LookupError(self.language_items.get("language_lookup_error", None) % key)
        if not isinstance(item, re._pattern_type): item = force_unicode(item.replace("\\n", "\n"))
        return item

if __name__ == "__main__":
    lang = language()
    lang.load("pt-br")
    print lang.language_items
    print lang["default_pattern"]
