#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
# Define the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)
try:
    # Send a GET request to the URL and open a connection
    with urllib.request.urlopen(request) as response:
        # Read the response content into the 'content' variable
        content = response.read()
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print("    - utf8 content:", content.decode("utf-8"))
except Exception as e:
    # Handle any exceptions that may occur during the request
    print("Error:", e)
