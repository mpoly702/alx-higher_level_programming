#!/usr/bin/python3
"""
Takes in a URL and an email address,Sends a POST request to the passed URL
with the email as a parameter
and finally displays the body of the response
"""


import sys
import requests


if __name__ == "__main__":
    address = sys.argv[1]
    email = sys.argv[2]
    info = [('email', email)]

    ans = requests.post(address, data=info)
    print(ans.text)
