#!/usr/bin/python3
""" sends and url and displays value"""
import requests
import sys

if __name__ == "__main__":
        listargs = sys.argv
        req = requests.get(listargs[1])
        if req.status_code > 400:
                print('Error code: {}'.format(req.status_code))
        else:
                print(req.text)
