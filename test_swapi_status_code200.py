import requests
import pytest

host = "https://swapi.py4e.com/api/"

def test_status_code():
    answer = requests.get(f"{host}/planets")
    assert answer.status_code == 200
