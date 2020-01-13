#!/usr/bin/python3
""" sends and url and displays value"""
import urllib.request
import sys

if __name__ == "__main__":
        try:
                listargs = sys.argv
                req = urllib.request.Request(listargs[1])
                with urllib.request.urlopen(req) as response:
                        html = response.read()
                print(html.decode('utf-8'))
        except urllib.error.HTTPError as e:
                print('Error code: {}'.format(e.code))
