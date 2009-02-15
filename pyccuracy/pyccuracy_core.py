from selenium_browser_driver import *
from story_runner import *
from test_fixture_parser import *
from language import *
from errors import *
	
class Pyccuracy(object):
	def run_tests(self, 
				  root=os.curdir, 
				  action_root=os.path.join(os.path.dirname(__file__), "actions"),
				  pattern="to_be_defined_by_language", 
				  browser_driver = SeleniumBrowserDriver(root_dir=os.curdir), 
				  default_language="en-us", 
				  languages_dir=os.path.join(os.path.dirname(__file__), "languages")):
				  
		lang = Language(languages_dir)
		lang.load(default_language)
		if (pattern == "to_be_defined_by_language"): pattern = lang["default_pattern"]
		self.current_browser_driver = browser_driver
		self.current_browser_driver.start()
		
		#parsing the tests
		fixture_parser = TestFixtureParser(self.current_browser_driver, lang, action_root)
		self.test_fixture = fixture_parser.get_fixture([file_path for file_path in locate(pattern, root)])
		
		#running the tests
		try:
			runner = StoryRunner(self.current_browser_driver, self.test_fixture)
			results = runner.run_stories()
		finally:
			self.current_browser_driver.stop()
		self.__print_results()
		
		if self.test_fixture.get_results().status == "FAILED":
			raise TestFailedError("The test failed!")
	
	def __print_results(self):
		print self.test_fixture.get_results()
		print "\n"

if __name__ == "__main__":
	pyc = Pyccuracy()
	pyc.run_tests(root=os.path.join(os.curdir, "tests/en_us"))
	pyc.run_tests(root=os.path.join(os.curdir, "tests/pt_br"), default_language="pt-br")
