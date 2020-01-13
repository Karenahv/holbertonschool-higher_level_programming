#!/usr/bin/python3
""" sends and url and displays value"""
import urllib.request
import urllib
import sys


listargs = sys.argv
req = urllib.request.Request(listargs[1])
with urllib.request.urlopen(req) as response:
    html = response.info()
print(html['X-Request-Id'])
