#!/usr/bin/python3
""" sends a POST"""
import requests
import sys

if __name__ == "__main__":
    films = {
         'https://swapi.co/api/films/2/': 'The Empire Strikes Back',
         'https://swapi.co/api/films/3/': 'Return of the Jedi',
         'https://swapi.co/api/films/7/': 'The Force Awakens',
         'https://swapi.co/api/films/5/': 'Attack of the Clones',
         'https://swapi.co/api/films/6/': 'Revenge of the Sith',
         'https://swapi.co/api/films/4/': 'The Phantom Menace',
         'https://swapi.co/api/films/1/': 'A New Hope'
         }
    url = 'https://swapi.co/api/people'
    listargs = sys.argv
    values = {'search': listargs[1]}
    req = requests.get(url, params=values)
    data1 = req.json()
    print("Number of results: {}".format(data1.get('count')))
    while True:
        for n in data1.get("results"):
            print(n.get('name'))
            for film in n.get('films'):
                print("\t{}".format(films.get(film)))
        if data1.get('next'):
            req = requests.get(data1.get('next'))
            data1 = req.json()
        else:
            break
