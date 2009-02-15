import unittest
import sys
import os
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.pyccuracy_core import *

class ActionTestBase(unittest.TestCase):
	def setUp(self):
		self.languages_to_test = ("en-us","pt-br") #add more here as languages grow
		self.pyccuracy = Pyccuracy()
		
	def get_root_dir(self, culture):
		return os.curdir
		
	def get_root_path(self):
		return os.path.abspath(__file__+"/../../../pyccuracy/")
		
	def get_languages_dir(self):
		return os.path.join(self.get_root_path(), "languages")
		
	def get_actions_path(self):
		return os.path.join(self.get_root_path(), "actions")
		
	def get_pattern(self, culture):
		return "*.acc"
	
	def run_tests(self):
	    for language in self.languages_to_test:
		    self.pyccuracy.run_tests(root = self.get_root_dir(language), 
									 default_language = language, 
									 pattern = self.get_pattern(language), 
									 languages_dir = self.get_languages_dir(),
									 action_root = self.get_actions_path())