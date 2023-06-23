import requests
import pytest

host = "https://swapi.py4e.com/api/"

def test_invalid_parameters():
    response = requests.get(f"{host}/planets/70")
    assert response.status_code == 404