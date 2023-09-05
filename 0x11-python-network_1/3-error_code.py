#!/usr/bin/python3
"""  Python script that takes in a URL, sends a request to the URL."""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
try:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
