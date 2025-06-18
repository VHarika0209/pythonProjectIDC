#webpage content
import socket
# Define the target host and port
host = "example.org"
port = 80
# Create a TCP socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server at the given host and port
client_socket.connect((host, port))
print(f"Connected to {host} on port {port}")
# Construct an HTTP GET request as a properly formatted string
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
# Send the request to the server, encoding it to bytes
client_socket.send(request.encode())
# Initialize a bytes object to hold the incoming response
response = b""
# Keep receiving data from the server until there's no more (recv returns empty)
while True:
    data = client_socket.recv(4096) # Receive in 4KB chunks
    if not data:
        break # Exit the loop when no more data is received
    response += data # Append received data to the response
# Close the socket to free up resources
client_socket.close()
# Find the start of the HTML content (after the headers, marked by \r\n\r\n)
html_start = response.find(b"\r\n\r\n")+4
# Extract only the HTML content and decode it into a readable string
html_content = response[html_start:].decode(errors="ignore")
# Print the webpage content retrieved from the server
print("Web Page Content:\n")
print(html_content)
