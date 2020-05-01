import socket
import pickle
# for sending object data

# handles the connection between server and client

class Network():
    def __init__(self):

        # .AF_INET is address family of IPv4 and .SOCK_STREAM is TCP socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # getting your IP address
        self.server = socket.gethostbyname(socket.gethostname())

        # setting port (any free port value can be used)
        self.port = 5555

        # creating address, a tuple of server(IP address) and port no. which will be used for binding and client connection
        self.addr = (self.server, self.port)

        self.p = self.connect()

    def getP(self):
        return self.p

    # connecting client
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    # sending data
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
