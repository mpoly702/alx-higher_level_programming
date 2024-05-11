#!/usr/bin/python3
"""
Takes in a URL,sends a request to the URL and displays
the body of the response(decoded in utf-8)
"""


import sys
from urllib import request, error


if __name__ == "__main__":
    address = sys.argv[1]
    try:
        with request.urlopen(address) as ans:
            c = ans.read()
            print(c.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
