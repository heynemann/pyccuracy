from windmill.authoring import WindmillTestClient
from browser_driver import *
from windmill.bin.admin_lib import configure_global_settings, setup
import windmill

class WindmillBrowserDriver(BrowserDriver):

    def __init__(self, browser_to_run, tests_dir):
        super(type(self),self).__init__(browser_to_run, tests_dir)
        self.__port__ = 4444
        self.__host__ = "localhost"
        configure_global_settings()
        windmill.settings['TEST_URL'] = 'localhost'#self.test_url
        if hasattr(self,"windmill_settings"):
            for (setting,value) in self.windmill_settings.iteritems():
                windmill.settings[setting] = value
        
#        self.client = WindmillTestClient(__name__)

#        self.controller = windmill.test_authoring.Controller('%s:%s' %(self.__host__,self.__port__))
#        self.controller.enable_unittest = True
#        self.controller.enable_assertions = False


