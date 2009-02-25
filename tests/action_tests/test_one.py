import unittest
from action_test_base import *

class TestOne(ActionTestBase):

    def set_pattern(self, pattern):
        self.pattern = pattern

    def get_pattern(self, culture):
        return "*%s_%s.acc" % (self.pattern, culture)

    def test_each_language(self, other):
        self.run_tests()

if __name__ == "__main__":
    test = TestOne("test_each_language")
    test.setUp()
    test.set_pattern(sys.argv[-1])
    runner = unittest.TextTestRunner()
    runner.run(test.test_each_language)

