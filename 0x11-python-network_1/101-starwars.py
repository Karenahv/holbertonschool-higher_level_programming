#!/usr/bin/python3
""" sends a POST"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    listargs = sys.argv
    values = {'search': listargs[1]}
    req = requests.get(url, params=values)
    data1 = req.json()
    print("Number of results: {}".format(data1.get('count')))
    while True:
        for n in data1.get("results"):
            print(n.get('name'))
        if data1.get('next'):
            req = requests.get(data1.get('next'))
            data1 = req.json()
        else:
            break
