#!/usr/bin/python3
"""
Takes in a URL and an email,Sends a POST request to the passed URL
With the email as a parameter
and displays the body of the response(decoded in utf-8)
"""


import sys
from urllib import request, parse


if __name__ == "__main__":
    address = sys.argv[1]
    email = sys.argv[2]
    info = bytes(parse.urlencode([('email', email)]), 'utf-8')

    with request.urlopen(address, data=info) as ans:
        c = ans.read()
        print(c.decode('utf-8'))
