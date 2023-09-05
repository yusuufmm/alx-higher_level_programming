#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request
if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:

    # Send a GET request to the URL and open a connection
    with urllib.request.urlopen(request) as response:
        # Read the response content into the 'content' variable
        with urllib.request.urlopen(request) as response:

        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
