#!/usr/bin/python3
""" sends a POST"""
import requests
import sys

if __name__ == "__main__":
    listargs = sys.argv
    values = {'email': listargs[2]}
    req = requests.post(listargs[1], data=values)
    print(req.text)
