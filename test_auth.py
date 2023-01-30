import requests
from data import *


def test_valid_auth():
    resp = requests.get(ENDPOINT + METHOD + "?" + API_KEY)
    data = resp.status_code
    assert data == successfully
    pass

def test_invalid_auth():
    resp = requests.get(ENDPOINT + METHOD + "?")
    data = resp.status_code
    assert data == fail_auth
    pass

#добавить тесты с "истекшим" ключом