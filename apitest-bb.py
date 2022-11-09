import requests
import json
import pprint
import logging
import os

def getPeople(headers):
        saved_people = open('jsonfiles/people.json', 'rt')
        people_data = json.load(saved_people)
        response = requests.request("GET", "https://swapi.dev/api/people", headers=headers, data = "")
        with open('jsonfiles/people2.json', 'wb')as people:
            people.write(response.content)
        actual_people = open('jsonfiles/people2.json', 'rt')
        actual_people_data = json.load(actual_people)
        print(people_data, actual_people_data)

        if people_data == actual_people_data:
            print('These JSONs are the same')
        else: 
            print('There are differences between these JSONs')
getPeople("")

""" def getPlanets(headers):
    response = requests.request("GET", "https://swapi.dev/api/planets", headers=headers, data = "")
    with open('jsonfiles/planets.json', 'wb')as planets:
        planets.write(response.content)

getPlanets("")

def getFilms(headers):
    response = requests.request("GET", "https://swapi.dev/api/films", headers=headers, data = "")
    with open('jsonfiles/films.json', 'wb')as films:
        films.write(response.content)

getFilms("")


def getSpecies(headers):
    response = requests.request("GET", "https://swapi.dev/api/species", headers=headers, data = "")
    with open('jsonfiles/species.json', 'wb')as species:
        species.write(response.content)

getSpecies("")

def getVehicles(headers):
    response = requests.request("GET", "https://swapi.dev/api/vehicles", headers=headers, data = "")
    with open('jsonfiles/vehicles.json', 'wb')as vehicles:
        vehicles.write(response.content)

getVehicles("")

def getStarships(headers):
    response = requests.request("GET", "https://swapi.dev/api/starships", headers=headers, data = "")
    with open('jsonfiles/starships.json', 'wb')as starships:
        starships.write(response.content)

getStarships("") """