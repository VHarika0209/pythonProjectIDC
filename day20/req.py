# Import the 'requests' library to handle HTTP requests easily
import requests
# Define the URL you want to send a GET request to
url = "http://httpbin.org/get"
# Send an HTTP GET request to the specified URL
response = requests.get(url)
print("status code : ", response.status_code)
print("Webpage Content:\n", response.content)
# Print the first 500 characters of the response as decoded text (HTML or JSON)
print(response.text[:500])