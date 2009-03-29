import asyncore
from asynchat import async_chat
import socket

class MainServerSocket(asyncore.dispatcher):
    def __init__(self, port):
        print "initializing MSS"
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', port))
        self.listen(5)
    
    def handle_accept(self):
        new_socket, address = self.accept()
        print "Connected from",address
        SecondaryServerSocket(new_socket)

class SecondaryServerSocket (async_chat):
    def __init__(self, *args):
        print "initializing SSS"
        async_chat.__init__(self, *args)
        self.set_terminator("\n")
        self.data = []
        
    def collect_incoming_data(self, data):
        self.data.append(data)
        
    def found_terminator(self):
        data_to_send = ''.join(self.data)
        print "Sending %s" % data_to_send
        self.push(data_to_send)
        self.data = []
        
    def handle_close(self):
        print "Disconnected from", self.getpeername()
        self.close()

if __name__ == "__main__":
    try:
        MainServerSocket(8882)
        asyncore.loop()
    except KeyboardInterrupt:
        print "Server finished..."
