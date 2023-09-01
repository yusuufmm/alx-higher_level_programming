#!/usr/bin/python3
import urllib.request

# Define the URL to fetch
url = "https://alx-intranet.hbtn.io/status"

try:
    # Send a GET request to the URL and open a connection
    with urllib.request.urlopen(url) as response:
        # Read the response content into the 'content' variable
        content = response.read()

        # Print information about the response
        print("Body response:")

        # Print the type of 'content' (bytes)
        print("    - type:", type(content))

        # Print the raw content (bytes)
        print("    - content:", content)

        # Print the content as UTF-8 (decoded bytes)
        print("    - utf8 content:", content.decode("utf-8"))
except Exception as e:
    # Handle any exceptions that may occur during the request
    print("Error:", e)
