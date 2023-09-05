#!/usr/bin/python3
"""  Python script that takes in a URL, sends a request to the URL."""
import sys
import urllib.error
import urllib.request
try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)