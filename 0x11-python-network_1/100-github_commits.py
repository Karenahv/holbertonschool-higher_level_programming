#!/usr/bin/python3
""" sends a POST"""
import requests
import sys

if __name__ == "__main__":
    listargs = sys.argv
    url = 'https://api.github.com/repos/' + listargs[2] + "/" +\
          listargs[1] + "/commits"
    req = requests.get(url)
    data = req.json()
    n = 0
    for commits in data:
        if n <= 9:
            print("{}: {}".format(commits.get("sha"),
                  commits.get("commit").get("author").get("name")))
            n = n + 1
