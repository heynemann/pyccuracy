from selenium_browser_driver import *
from story_runner import *
from test_fixture_parser import *
from language import *
	
class Pyccuracy:
	def run_tests(self, root=os.curdir, pattern="to_be_defined_by_language", browser_driver = SeleniumBrowserDriver(), default_language="en-us"):
		lang = Language()
		lang.load(default_language)
		if (pattern == "to_be_defined_by_language"): pattern = lang["default_pattern"]
		self.current_browser_driver = browser_driver
		self.current_browser_driver.start()
		
		#parsing the tests
		fixture_parser = TestFixtureParser(self.current_browser_driver, lang)
		self.test_fixture = fixture_parser.get_fixture([file_path for file_path in locate(pattern, root)])
		
		#running the tests
		try:
			runner = StoryRunner(self.current_browser_driver, self.test_fixture)
			results = runner.run_stories()
		finally:
			self.current_browser_driver.stop()
		self.__print_results()
	
	def __print_results(self):
		print self.test_fixture

if __name__ == "__main__":
	pyc = Pyccuracy()
	pyc.run_tests(root=os.path.join(os.curdir, "tests/en_us"))
	pyc.run_tests(root=os.path.join(os.curdir, "tests/pt_br"), default_language="pt-br")
