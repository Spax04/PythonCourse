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

    # Your code here

    def connect(self):

    # Your code here

    def send_message(self, message):

    # Your code here

    def receive_message(self):

    # Your code here

    def close(self):


# Your code here


# Example usage
client = ChatClient('localhost', 5000)
client.connect()

message = input("Enter a message to send: ")
client.send_message(message)

received_message = client.receive_message()
print("Received message:", received_message)

client.close()

