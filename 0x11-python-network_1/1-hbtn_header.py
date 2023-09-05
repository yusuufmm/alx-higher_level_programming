#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL. """
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
