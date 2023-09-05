#!/usr/bin/python3
""" Python script that takes in a URL and an email address, sends a POST. """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    y = requests.post(url, data=value)
    print(y.text)