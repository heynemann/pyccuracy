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
"""
ACC_DIR = "%s/acceptance/" % os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.realpath(os.curdir)
SEL_DIR = os.path.dirname(selenium.__file__)

class PyccuracyTestCase(TestCase):
    sel_server = None
    app_server = None

    def runSeleniumServer(self):
        sel_server_path = SEL_DIR
        sel_command = ["java", "-jar", "lib/selenium-server.jar"]
        self.sel_server = Popen(sel_command, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=sel_server_path)

        #wait selenium rc to be ready
        line = self.sel_server.stdout.readline()
        while not "Started SocketListener on" in line:
            line = self.sel_server.stdout.readline()
        print "Started selenium server"

    def runApplicationServer(self):
        app_server_path = APP_DIR
        self.app_server = Popen(['python', 'manage.py', 'runserver'],
                stdout=PIPE, stderr=STDOUT, cwd=app_server_path)
        time.sleep(2) #FIXME: we need to wait for the server to be ready
        print "Application Server started"

    def setUp(self):
        """Starts the application and selenium servers"""

        self.runApplicationServer()
        self.runSeleniumServer()

    def tearDown(self):
        """Stops Selenium RC and Django Server."""
        self.sel_server.terminate()
        self.app_server.terminate()

    def testAcceptanceWithPyccuracy(self):
        """Execute acceptance tests running Pyccuracy Core"""
        core = PyccuracyCore()
        result = core.run_tests(
                #base_url="http://myserver/index",
                tests_dir= ACC_DIR,
                write_report=False,
                browser_to_run="firefox",
                browser_driver="selenium",
                should_throw="should_throw",
                workers=1,
                verbosity=2,)

