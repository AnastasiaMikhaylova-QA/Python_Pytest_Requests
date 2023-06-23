import requests
import pytest

host = "https://swapi.py4e.com/api/"

def test_planet_name():
    answer = requests.get(f"{host}/planets/10")
    assert answer.json()["name"] == "Kamino"