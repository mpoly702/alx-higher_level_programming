#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """


import requests


if __name__ == "__main__":
    address = 'https://alx-intranet.hbtn.io/status'
    ans = requests.get(address)
    print("Body response:")
    print("\t- type: {}".format(type(ans.text)))
    print("\t- content: {}".format(ans.text))
