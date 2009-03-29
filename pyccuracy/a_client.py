import xmlrpclib
import urlparse
from uuid import uuid4
import time
import socket

class PyccuracyClient (object):

    def __init__(self,addr):
        urlparse.uses_netloc.append("pycc")
        self.url = urlparse.urlparse(addr)


    def listen(self):
    
        user_id = uuid4()
        print "Trying to identify as %s" % user_id
        
        try:
            svr = xmlrpclib.ServerProxy('http://%s:%s' %(self.url.hostname,self.url.port))
            print svr.identify_as(str(user_id))
            
            for i in xrange(20):
                print "Trying to get test number %d" % i
                response = svr.get_next_test_message()
                print "Server responded: %s" % response
                time.sleep(2)
        except socket.error:
            print '\nServer Hang Unexpectedly'
        
if __name__ == "__main__":

    c = PyccuracyClient('pycc://localhost:101977/test1')
    c.listen()

# Print list of available methods
#print s.system.listMethods()
