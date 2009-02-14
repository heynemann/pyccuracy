import unittest
from action_test_base import *

class TestDoNotSeeSelect(ActionTestBase):
		
	def get_pattern(self, culture):
		return "test_do_not_see_select_%s.acc" % culture
	
	def test_each_language(self):
		self.run_tests()
	
if __name__ == "__main__":
    unittest.main()
