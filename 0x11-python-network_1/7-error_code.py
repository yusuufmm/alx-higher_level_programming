#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL ."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    u = requests.get(url)
    if u.status_code >= 400:
        print("Error code: {}".format(u.status_code))
    else:
        print(u.text)
