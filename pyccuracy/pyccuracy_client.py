import socket

buffer_size = 8192

def write_lines():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8882))
    print "Connected to Server"
    data = """A few lines of data
    to test the operation
    of both server and client"""
    
    for line in data.splitlines():
        sock.sendall(line + "\n")
        print "Sent %s" % line
        response = sock.recv(buffer_size)
        print "Received %s" % response
        
    sock.close()

if __name__ == "__main__":
    write_lines()
