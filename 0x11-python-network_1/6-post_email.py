#!/usr/bin/python3
"""Takes in a URL and an email address, sends a
POST request to the passed URL with the email
"""
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    req = requests.post(sys.argv[1], data={'email': email})
    print(req.text)
