#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """


import urllib.request


if __name__ == "__main__":
    address = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(address) as ans:
        info = ans.read()
        print("Body response:")
        print("\t- type: {}".format(type(info)))
        print("\t- content: {}".format(info))
        print("\t- utf8 content: {}".format(info.decode('utf-8')))
