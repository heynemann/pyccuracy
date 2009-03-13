import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.pyccuracy_core import *

class ActionTestBase(unittest.TestCase):
    def setUp(self):
        self.languages_to_test = ("en-us","pt-br") #add more here as languages grow
        self.pyccuracy = PyccuracyCore()

    def get_root_dir(self, culture):
        return os.path.abspath(os.path.split(__file__)[0])

    def get_root_path(self):
        return os.path.abspath(__file__+"/../../../pyccuracy/")

    def get_languages_dir(self):
        return os.path.join(self.get_root_path(), "languages")

    def get_pattern(self, culture):
        return "*.acc"

    def run_tests(self):
        for language in self.languages_to_test:
            self.pyccuracy.run_tests(tests_path = self.get_root_dir(language), 
                                     default_culture = language, 
                                     file_pattern = self.get_pattern(language), 
                                     languages_dir = self.get_languages_dir(),
                                     should_throw = True)
