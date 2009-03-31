import windmill
from browser_driver import *

class WindmillBrowserDriver(BrowserDriver):

    def __init__(self, browser_to_run, tests_dir):
        super(type(self),self).__init__(browser_to_run, tests_dir)
        self.__port__ = 4444
        self.__host__ = "localhost"
        self.controller = windmill.test_authoring.Controller('%s:%s' %(self.__host__,self.__port__))
        self.controller.enable_unittest = True
        self.controller.enable_assertions = False


