import socket
import time
from uuid import uuid4
from pyccuracy_distributed_language import *

def write_lines():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', DEFAULT_PORT))
        
        user_id = uuid4()
        print "Trying to identify as %s" % user_id
        sock.sendall(identify_message % user_id)
        response = sock.recv(BUFFER_SIZE)
        print "Server responded: %s" % response

        for i in range(20):
            print "Trying to get test number %d" % i
            sock.sendall(get_next_test_message)
            response = sock.recv(BUFFER_SIZE)
            print "Server responded: %s" % response
            
            test_number = response[-12:]
            test_result = i % 2 == 0 and "SUCCESSFUL" or "FAILED"
            print "sending result for test %s of %s" % (test_number, test_result)
            sock.sendall(send_result_message % (test_number, test_result))
            response = sock.recv(BUFFER_SIZE)
            print "Server responded: %s" % response
            time.sleep(2)

        sock.close()
    except socket.error:
        print "Server Hangup Unexpectedly"
        
if __name__ == "__main__":
    write_lines()
