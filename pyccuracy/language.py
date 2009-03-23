# -*- coding: utf-8 -*-

from errors import *
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

        for line in lines:
            if not line.startswith("#"):
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                if key.endswith("_regex"):
                    value = re.compile(value, re.U)
                self.language_items[key.strip()] = value

    def __getitem__(self, key):
        item = self.language_items.get(key, None)
        if item is None: raise LookupError("The key %s was not found in the language definitions." % key)
        return item

if __name__ == "__main__":
    lang = language()
    lang.load("pt-br")
    print lang.language_items
    print lang["default_pattern"]
