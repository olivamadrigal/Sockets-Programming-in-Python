# client script
import socket

server_ip = '127.0.0.1'
server_port = 55555

buffer_size = 1024
# create end point
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to socket
s.connect((server_ip, server_port))
i = 0

done = False
while not done:
    # receive data from server similar to HW1
    data = s.recv(buffer_size)
    # write this to a file
    message = data.decode('utf-8')
    print(message)
    if message == "EOF":
        done = True
