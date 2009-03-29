import sys
import asyncore
import socket
from uuid import uuid4
from pyccuracy_distributed_language import *

class PyccuracyServer(object):
    def __init__(self, port):
        self.port = port

    def start(self):
        try:
            self.server_socket = PyccuracyServerMainSocket(DEFAULT_PORT)
            asyncore.loop()
        except KeyboardInterrupt:
            print "Server Finished"
            sys.exit(0)
        
class PyccuracyServerMainSocket(asyncore.dispatcher):
    def __init__(self, port):
        self.port = port
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
        self.server_socket = PyccuracyServerSecondarySocket(self.current_socket)

class PyccuracyServerSecondarySocket(asyncore.dispatcher_with_send):
    def __init__(self, socket):
        asyncore.dispatcher_with_send.__init__(self, socket)
        self.factory = PyccuracyServerFactory(self.send)
        
    def handle_close(self):
        pass
        
    def handle_read(self):
        received_data = self.recv(BUFFER_SIZE)
        if received_data:
            self.factory.route(received_data)

class PyccuracyServerFactory(object):
    def __init__(self, send_method):
        self.send = send_method
    
    def route(self, message):
        print "Routing message: %s" % message
        if message.startswith(identify_action):
            action, user_id = message.split(':')
            self.handle_identify(user_id)
        if message.startswith(get_next_test_action):
            action = message
            self.handle_next_test()

    def handle_identify(self, user_id):
        self.identity = user_id
        print "Identified %s correctly." % user_id
        self.send("Identity granted at user %s" % self.identity)
        
    def handle_next_test(self):
        test_number = uuid4()
        print "Sending test number %s..." % test_number
        self.send("You got your test mofo: %s" % test_number)
        print "Test sent!"

if __name__ == "__main__":
    srv = PyccuracyServer(DEFAULT_PORT)
    srv.start()
