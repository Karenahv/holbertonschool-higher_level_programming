#!/usr/bin/python3
""" sends a POST"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    listargs = sys.argv
    values = {'email': listargs[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode()
    req = urllib.request.Request(listargs[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    print(html)
