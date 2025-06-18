import socket
import time

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server on localhost (same machine) at port 65432
client_socket.connect(('localhost', 65432))
# Send a message to the server (encoded as UTF-8 bytes)
client_socket.send("Hello from client!".encode('utf-8'))
# Wait to receive a response from the server (up to 1024 bytes)
response = client_socket.recv(1024).decode('utf-8')
print("Server response: ", response)
# Pause the execution for 2 seconds before closing the connection (optional, just to simulate delay)
time.sleep(2)
# Close the socket to end the connection gracefully
client_socket.close()
