# -*- coding: utf-8 -*-
#
# Authors:
# Flávio Amieiro <amieiro.flavio@gmail.com>
# Henrique Bastos <henrique@bastos.net>
#
# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.opensource.org/licenses/osl-3.0.php
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import time
from subprocess import Popen, STDOUT, PIPE
from django.test import TestCase
from pyccuracy.core import PyccuracyCore
import selenium

"""
Path constants
You will need to configure the Path Constants according to your directory layout.

BASE_PATH
  Is Djangucacy's absolute path

APPLICATION_DIR
  Is the Django App directory (contains manage.py)

SELENIUM_DIR
  Is the directory of Selenium RC. We expect it contains the python driver and a lib subdirectory containing the RC Jar library.
"""
APPLICATION_DIR     = os.path.realpath(os.curdir)
SELENIUM_DIR        = os.path.dirname(selenium.__file__)

BASE_PATH           = os.path.dirname(os.path.realpath(__file__))
ACC_TESTS_DIR       = "%s/acceptance/" % BASE_PATH
CUSTOM_ACTIONS_DIR  = "%s/custom_actions/" % BASE_PATH
CUSTOM_PAGES_DIR    = "%s/custom_pages/" % BASE_PATH
LOG_SELENIUM        = "%s/selenium.log" % BASE_PATH
LOG_APPLICATION     = "%s/application.log" % BASE_PATH

class PyccuracyTestCase(TestCase):
    application_server = None
    selenium_server = None

    def runApplicationServer(self):
        """Starts Django Test Server"""
        logfile = open(LOG_APPLICATION, 'w')
        self.application_server = Popen(['python', 'manage.py', 'testserver'],
                stdout=logfile, stderr=STDOUT, cwd=APPLICATION_DIR)
        time.sleep(5) #FIXME: we need to wait for the server to be ready
        print "Started Django Test Server"

    def runSeleniumServer(self):
        """Starts Selenium RC server"""
        command = ["java", "-jar", "lib/selenium-server.jar"]
        logfile = open(LOG_SELENIUM, 'w')

        self.selenium_server = Popen(command, stdin=PIPE, 
              stdout=logfile, stderr=STDOUT, cwd=SELENIUM_DIR)

        #wait selenium rc to be ready
        with open(LOG_SELENIUM, 'r') as f:
           line = f.readline()
           while not "Started SocketListener on" in line:
              line = f.readline()
           print "Started Selenium RC Server"

    def setUp(self):
        """Starts Django Test Server and Selenium RC Server."""
        self.runApplicationServer()
        self.runSeleniumServer()

    def tearDown(self):
        """Stops Django Test Server and Selenium RC."""
        self.application_server.terminate()
        self.selenium_server.terminate()

    def testAcceptanceWithPyccuracy(self):
        """Execute acceptance tests running Pyccuracy Core"""
        core = PyccuracyCore()
        result = core.run_tests(
                #base_url="http://myserver/index",
                tests_dir=ACC_TESTS_DIR,
                custom_actions_dir=CUSTOM_ACTIONS_DIR,
                pages_dir=CUSTOM_PAGES_DIR,
                write_report=False,
                default_culture="pt-br",
                browser_to_run="firefox",
                browser_driver="selenium",
                should_throw="should_throw",
                workers=1,
                verbosity=2,)

