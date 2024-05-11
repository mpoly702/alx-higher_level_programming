#!/usr/bin/python3
"""
Takes in a URL,sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""


import sys
import requests


if __name__ == '__main__':
    address = sys.argv[1]
    ans = requests.get(address)

    print(ans.headers.get('X-Request-Id'))
