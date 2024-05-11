#!/usr/bin/python3
"""
Lists 10 the 10 most recent commits
Of a given repository by the user
"""


import sys
import requests


if __name__ == "__main__":
    address = 'https://api.github.com/repos/{}/{}/commits'
    ans = requests.get(address.format(sys.argv[2], sys.argv[1]))
    info = ans.json()

    for commit in info[:10]:
        sha = commit['sha']
        can = commit['commit']['author']['name']
        print("{}: {}".format(sha, can))
