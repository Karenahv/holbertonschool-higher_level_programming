#!/usr/bin/python3
""" sends a POST"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    listargs = sys.argv
    req = requests.get(url, auth=(listargs[1], listargs[2]))
    data = req.json()
    print(data.get('id'))
