import unittest
from action_test_base import *

class TestPageWaitForPageToLoad(ActionTestBase):
		
	def get_pattern(self, culture):
		return "test_page_wait_for_page_to_load_%s.acc" % culture
	
	def test_each_language(self):
		self.run_tests()
	
if __name__ == "__main__":
    unittest.main()
