import unittest
from action_test_base import *

class TestSeeButton(ActionTestBase):
		
	def get_pattern(self, culture):
		return "test_see_button_%s.acc" % culture
	
	def test_each_language(self):
		for language in self.languages_to_test:
			self.pyccuracy.run_tests(root = self.get_root_dir(language), 
									 default_language = language, 
									 pattern = self.get_pattern(language), 
									 languages_dir = self.get_languages_dir(),
									 action_root = self.get_actions_path())
	
if __name__ == "__main__":
    unittest.main()
