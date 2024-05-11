#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import sys
import requests


if __name__ == "__main__":
    address = "https://api.github.com/user"
    ans = requests.get(address, auth=(sys.argv[1], sys.argv[2]))

    if ans.status_code == 200:
        info = ans.json().get('id')
        print(info)
    else:
        print("None")
