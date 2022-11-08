import requests
import json
import pprint

def getPeople(headers):
    response = requests.request("GET", "https://swapi.dev/api/people", headers=headers, data = "")
    with open('jsonfiles/people.json', 'wb')as f:
        f.write(response.content)

getPeople("")

def getPlanets(headers):
    response = requests.request("GET", "https://swapi.dev/api/planets", headers=headers, data = "")
    with open('jsonfiles/planets.json', 'wb')as f:
        f.write(response.content)

getPlanets("")

def getFilms(headers):
    response = requests.request("GET", "https://swapi.dev/api/films", headers=headers, data = "")
    with open('jsonfiles/films.json', 'wb')as f:
        f.write(response.content)

getFilms("")


def getSpecies(headers):
    response = requests.request("GET", "https://swapi.dev/api/species", headers=headers, data = "")
    with open('jsonfiles/species.json', 'wb')as f:
        f.write(response.content)

getSpecies("")

def getVehicles(headers):
    response = requests.request("GET", "https://swapi.dev/api/vehicles", headers=headers, data = "")
    with open('jsonfiles/vehicles.json', 'wb')as f:
        f.write(response.content)

getVehicles("")

def getStarships(headers):
    response = requests.request("GET", "https://swapi.dev/api/starships", headers=headers, data = "")
    with open('jsonfiles/starships.json', 'wb')as f:
        f.write(response.content)

getStarships("")