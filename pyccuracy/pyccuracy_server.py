#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import asyncore
import socket
import optparse
import Queue
from uuid import uuid4
from pyccuracy_distributed_language import *
from pyccuracy.pyccuracy_core import PyccuracyCore

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

u"""Pyccuracy - BDD Acceptance Testing Server

Example usage
=============

    python pyccuracy_server.py

:author: `Bernardo Heynemann <mailto:heynemann@gmail.com>`__
"""

# Pylint checks
# "line to long" pylint: disable-msg=C0301
# "Used * or ** magic" pylint: disable-msg=W0142

__revision__ = "$Id$"
__docformat__ = 'restructuredtext en'

def main():
    """ Main function - parses args and runs action """
    parser = optparse.OptionParser(usage="%prog or type %prog -h (--help) for help", description=__doc__, version="%prog" + __revision__)
    parser.add_option("-p", "--pattern", dest="pattern", default="*.acc", help="File pattern. Defines which files will get executed [default: %default].")
    parser.add_option("-l", "--language", dest="language", default="en-us", help="Language. Defines which language the dictionary will be loaded with  [default: %default].")
    parser.add_option("-L", "--languagesdir", dest="languages_dir", default=None, help="Languages Directory. Defines where Pyccuracy will search for language dictionaries  [default: %default].")
    parser.add_option("-d", "--dir", dest="dir", default=os.curdir, help="Tests directory. Defines where the tests to be executed are [default: %default]. Note: this is recursive, so all the tests under the current directory get executed.")
    parser.add_option("-a", "--actionsdir", dest="actions_dir", default=None, help="Actions directory. Defines where the Pyccuracy actions are. Chances are you don't need to change this parameter [default: %default].")
    parser.add_option("-A", "--customactionsdir", dest="custom_actions_dir", default=None, help="Custom Actions directory. Defines where the Pyccuracy custom actions are. If you don't change this parameter Pyccuracy will use the tests directory [default: %default].")
    parser.add_option("-P", "--pagesdir", dest="pages_dir", default=None, help="Pages directory. Defines where the Pyccuracy custom pages are. If you don't change this parameter Pyccuracy will use the tests directory [default: %default].")
    parser.add_option("-u", "--url", dest="url", default=None, help="Base URL. Defines a base url against which the tests will get executed. For more details check the documentation [default: %default].")
    parser.add_option("-b", "--browser", dest="browser_to_run", default="firefox", help="Browser to run. Browser driver will use it to run tests [default: %default].")
    
    #browser driver
    parser.add_option("-e", "--browserdriver", dest="browser_driver", default="selenium", help="Browser Driver to be used on tests. [default: %default].")

    #throws
    parser.add_option("-T", "--throws", dest="should_throw", default=False, help="Should Throw. Defines whether Pyccuracy console should throw an exception when tests fail. This is useful to set to True if you are running Pyccuracy inside unit tests [default: %default].")

    #reporter
    parser.add_option("-R", "--report", dest="write_report", default="true", help="Should write report. Defines if Pyccuracy should write an html report after each run [default: %default].")
    parser.add_option("-D", "--reportdir", dest="report_dir", default=os.curdir, help="Report directory. Defines the directory to write the report in [default: %default].")
    parser.add_option("-F", "--reportfile", dest="report_file_name", default="report.html", help="Report file. Defines the file name to write the report with [default: %default].")
    
    #server
    parser.add_option("-o", "--port", dest="port", default=DEFAULT_PORT, help="Server Port. Defines the port that the server will listen at [default: %default].")
    (options, args) = parser.parse_args()

    pyc = PyccuracyServer(port=options.port)

    pyc.start(actions_dir=options.actions_dir,
                       custom_actions_dir=options.custom_actions_dir,
                       pages_dir=options.pages_dir,
                       languages_dir=options.languages_dir,
                       file_pattern=options.pattern,
                       tests_dir=options.dir,
                       base_url=options.url,
                       default_culture=options.language,
                       write_report=options.write_report.lower() == "true",
                       report_file_dir=options.report_dir,
                       report_file_name=options.report_file_name,
                       browser_to_run=options.browser_to_run,
                       browser_driver=options.browser_driver,
                       should_throw=options.should_throw)

class PyccuracyServer(object):
    def __init__(self, port):
        self.port = port

    def start(self,
              actions_dir,
              custom_actions_dir,
              pages_dir,
              languages_dir,
              file_pattern,
              tests_dir,
              base_url,
              default_culture,
              write_report,
              report_file_dir,
              report_file_name,
              browser_to_run,
              browser_driver,
              should_throw):
        try:
            core = PyccuracyCore()
            core.configure_context(tests_dir,
                                   actions_dir,
                                   custom_actions_dir,
                                   pages_dir,
                                   file_pattern,
                                   default_culture,
                                   languages_dir,
                                   base_url,
                                   should_throw,
                                   None,
                                   write_report,
                                   report_file_dir,
                                   report_file_name,
                                   browser_to_run,
                                   browser_driver)

            self.server_socket = PyccuracyServerMainSocket(DEFAULT_PORT, core)
            asyncore.loop()
        except KeyboardInterrupt:
            print "Server Finished"
            sys.exit(0)
        
class PyccuracyServerMainSocket(asyncore.dispatcher):
    def __init__(self, port, core):
        self.port = port
        self.core = core
        asyncore.dispatcher.__init__(self)
        print "initializing Server Sockets..."
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind(('', self.port))
        self.listen(5)
        print "Server Sockets initialized."

    def handle_accept(self):
        print "Receiving Connection..."
        new_socket, address = self.accept()
        self.current_socket = new_socket
        self.server_socket = PyccuracyServerSecondarySocket(self.current_socket, self.core)

class PyccuracyServerSecondarySocket(asyncore.dispatcher_with_send):
    def __init__(self, socket, core):
        asyncore.dispatcher_with_send.__init__(self, socket)
        self.factory = PyccuracyServerFactory(self.send, core)
        
    def handle_close(self):
        pass
        
    def handle_read(self):
        received_data = self.recv(BUFFER_SIZE)
        if received_data:
            self.factory.route(received_data)

class PyccuracyServerFactory(object):
    def __init__(self, send_method, core):
        self.send = send_method
        self.core = core
        self.build_tests_queue()
    
    def build_tests_queue(self):
        self.queue = Queue.Queue()
        for story in self.core.context.test_fixture.stories:
            story.uuid = uuid4()
            self.queue.put(story)
    
    def route(self, message):
        print "Routing message: %s" % message
        if message.startswith(identify_action):
            action, user_id = message.split(':')
            self.handle_identify(user_id)
        elif message.startswith(get_next_test_action):
            action = message
            self.handle_next_test()
        elif message.startswith(send_result_action):
            action, result = message.split(':')
            test_id, status = result.split('=')
            self.handle_test_result(test_id, status)

    def handle_identify(self, user_id):
        self.identity = user_id
        print "Identified %s correctly." % user_id
        self.send("Identity granted at user %s" % self.identity)
        
    def handle_next_test(self):
        try:
            story = self.queue.get()
            import pdb;pdb.set_trace()
            print "Sending story"
            self.send(sending_test_message % story.serialize())
            print "Story sent!"
        except Queue.Empty:
            print "No more tests to run"
            self.send(no_more_tests_message)
        
    def handle_test_result(self, test_id, status):
        print "Received result for test %s of %s" % (test_id, status)
        self.send("Your result got computed for test %s" % test_id)
        print "Informed client of acceptance"
        
if __name__ == "__main__":
    main()
    #srv = PyccuracyServer(DEFAULT_PORT)
    #srv.start()
