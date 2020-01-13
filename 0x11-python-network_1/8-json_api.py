#!/usr/bin/python3
""" sends a POST"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        listargs = sys.argv
        values = {'q': listargs[1]}
    else:
        values = {'q': ""}
    try:
        req = requests.post(url, data=values)
        data1 = req.json()
        if not data1:
            print("No result")
        else:
            print("[{}] {}".format(data1.get('id'), data1.get('name')))
    except ValueError:
        print("Not a valid JSON")
