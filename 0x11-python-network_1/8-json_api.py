#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import sys
import requests


if __name__ == "__main__":
    address = sys.argv[1] if len(sys.argv) > 1 else ""
    msg = {'q': address}
    addr = 'http://0.0.0.0:5000/search_user'
    ans = requests.post(addr, data=msg)

    try:
        info = ans.json()
        if info:
            print("[{}] {}".format(info.get('id'), info.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
