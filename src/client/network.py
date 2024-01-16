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
        """
        Connects to the server.
        :return: The validation message form the server.
        """
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        """
        Sends data to the server. After sending the data, the network will wait for a ressponse.
        :param data: The data to be sent.
        :return: The response from the server, usually an object.
        """
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
            # return self.client.recv(2048).decode() DEBUG ONLY
        except socket.error as e:
            print(e)

    def send_without_response(self, data):
        """
        Sends data to the server. In this case, the network will not wait for a response from the server.
        :param data: The data to be sent.
        :return: None
        """
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)

    def close(self):
        """
        Closes the connection with the server.
        :return: None
        """
        self.client.close()
