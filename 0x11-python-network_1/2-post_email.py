#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    args = sys.argv
    data_encoded = urllib.parse.urlencode({'email': args[2]}).encode("utf-8")
    post_request = urllib.request.Request(args[1], data_encoded, method="POST")
    with urllib.request.urlopen(post_request) as response:
        content = response.read().decode("utf-8")
        print(content)
