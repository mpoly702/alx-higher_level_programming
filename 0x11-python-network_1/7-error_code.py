#!/usr/bin/python3
"""
Takes in a URL,sends a request to the URL
and displays the body of the response
"""


import sys
import requests


if __name__ == "__main__":
    address = sys.argv[1]
    ans = requests.get(address)

    if ans.status_code >= 400:
        print('Error code: {}'.format(ans.status_code))
    else:
        print(ans.text)
