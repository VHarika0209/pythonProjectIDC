#server.py
import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind to address and port
server_socket.bind(('localhost', 65432))

#Start listening
server_socket.listen()
print("Waiting for connection...")

#Accept connection
connection, client_address  = server_socket.accept()
print("Connection from : ", client_address)

#Receive data from client
incoming = connection.recv(1024).decode('utf-8')
print("Client sent :", incoming)

#Send reply
connection.send("Hello from server!!".encode('utf-8'))

#Close connection
connection.close()