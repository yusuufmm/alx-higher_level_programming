#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode(value).encode("ascii")
    data = data.encode('utf-8')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
