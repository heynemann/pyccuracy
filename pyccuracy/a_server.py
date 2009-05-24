import os
import sys
import urlparse
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import datetime
from uuid import uuid4

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    
class PyccuracyServer(object):

    def __init__(self, addr):
        urlparse.uses_netloc.append("pycc")
        self.url = urlparse.urlparse(addr)

    def start(self):
        try:
 
            self.server = SimpleXMLRPCServer((self.url.hostname, self.url.port), requestHandler=RequestHandler)
            self.server.RequestHandlerClass.rpc_paths.__add__(tuple(self.url.path))
            
            self.server.register_introspection_functions()

            self.register_functions()
            
            self.server.serve_forever()
        except KeyboardInterrupt:
            print "\nServer Finished"
            sys.exit(0)            

    def register_functions(self):
        self.server.register_function(self.get_next_test_action)
        self.server.register_function(self.get_next_test_message)
        self.server.register_function(self.handle_identify,"identify_as")

    def handle_identify(self, user_id):
        self.identity = user_id
        print "Identified %s correctly." % user_id
        return "Identity granted at user %s" % str(self.identity)

    def get_next_test_action(self):
        return datetime.datetime.now()
        
    def get_next_test_message(self):
        test_number = uuid4()
        print "Sending test number %s..." % test_number
        return str(test_number)

if __name__ == '__main__':
	m = PyccuracyServer('pycc://localhost:101977/test1')
	m.start()
	
	
