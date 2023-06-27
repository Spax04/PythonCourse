#
# Create a class named ChatClient that represents a simple chat client using sockets. This class should have the following functionality:
#
# 1.	The ChatClient class should have an __init__ method that takes two parameters: host and port. These parameters represent the host and port number of the server that the client will connect to.
# 2.	The ChatClient class should have a method named connect that establishes a connection to the server using the provided host and port.
# 3.	The ChatClient class should have a method named send_message that takes a message as a parameter and sends it to the server.
# 4.	The ChatClient class should have a method named receive_message that receives a message from the server and returns it.
# 5.	The ChatClient class should have a method named close that closes the connection to the server.
#
# Your task is to implement the ChatClient class with the described functionality.
# Instructions:

import socket


class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except socket.error as e:
            print(f"Connection error: {str(e)}")

    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode())
            print("Message sent successfully.")
        except socket.error as e:
            print(f"Error sending message: {str(e)}")

    def receive_message(self):
        try:
            message = self.client_socket.recv(1024).decode()
            return message
        except socket.error as e:
            print(f"Error receiving message: {str(e)}")
            return None

    def close(self):
        try:
            self.client_socket.close()
            print("Connection closed.")
        except socket.error as e:
            print(f"Error closing connection: {str(e)}")


# Example usage
client = ChatClient('192.168.12.12', 12345)
client.connect()

message = input("Enter a message to send: ")
client.send_message(message)

received_message = client.receive_message()
if received_message:
    print("Received message:", received_message)

client.close()

