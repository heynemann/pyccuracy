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

        if not os.path.exists(file_path): raise LanguageParseError(culture, file_path)
        try:
            fsock = open(file_path)
            lines = [line.strip() for line in fsock.readlines() if line.strip() != ""]
            fsock.close()
        except ValueError:
            raise LanguageParseError(culture)

        for line in lines:
            if not line.startswith("#"):
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                if key.endswith("_regex"):
                    value = re.compile(value)
                self.language_items[key.strip()] = value

    def __getitem__(self, key): 
        if self.language_items.has_key(key):
            return self.language_items[key]
        return None

if __name__ == "__main__":
    lang = language()
    lang.load("pt-br")
    print lang.language_items
    print lang["default_pattern"]
