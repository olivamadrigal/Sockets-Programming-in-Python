# HW #2 Simple TCP Server
# For this assignment, build and demonstrate a TCP server similar to the HW#1, service provided at 94.142.241.111
# Nothing too complicated, ‘Hello World’ in ASCII art is acceptable
# Submit: a Word document with some screenshots of the output, and a link to your source code
# There will be a prize for the best / most interesting submission
# Server Serves Harry Potter ASCII ART: https://www.asciiart.eu/books/harry-potter
# server script
import socket
import sys
from base64 import *

# USE LOCAL SERVER
HOST = '127.0.0.1'
PORT = 55555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the well-known port
server_address = ('localhost', PORT)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)  # at most 1 client

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
        while True:
            f = open("harrypotter.txt", "r")
            for line in f:
                encoded_msg = bytes(line, 'utf-8')
                connection.sendall(encoded_msg)
            encoded_msg = bytes("EOF", 'utf-8')
            connection.sendall(encoded_msg)
    finally:
        # Clean up the connection
        connection.close()
