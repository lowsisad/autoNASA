import requests
from data import *

resp = requests.get(ENDPOINT + METHOD + "?" + tooOld)
message = resp.json()
print(message)

def test_valid_date():
    resp = requests.get(ENDPOINT + METHOD + "?" + API_KEY + "&date=" + normal)
    data = resp.status_code
    assert data == successfully
    pass

def test_invalid_date():
    resp = requests.get(ENDPOINT + METHOD + "?" + API_KEY + "&date=" + future)
    data = resp.status_code
    resp = resp.json()
    msg = resp['msg']
    assert data == fail
    assert msg == future_msg
    pass

#сделать тесты со всеми вариантами из группы dates