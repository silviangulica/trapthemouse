import socket
import pickle


class Network:
    """
    Network class for client-server communication using sockets.
    On connection, the server will send the player what mode he will play with.
    """

    def __init__(self):
        """
        Initializes the network class with the socket and the server address.
        The default port is 5555.
        The default server address is localhost.
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
            # return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
