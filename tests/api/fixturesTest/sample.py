import pytest 
import requests

@pytest.fixture(autouse=use)
def quickCheck(setting_up_baseurl):
    assert requests.get(setting_up_baseurl).status_code ==200


@pytest.fixture()
def setting_up_baseurl():
    return "http://139.59.91.96:9000/v1/"

@pytest.fixture
def payload():
    return {"username":"iamfd", "password": "password"}

@pytest.fixture
def header():
    return {"content-type":"application/json"}


def makeLoginRequest(setting_up_baseurl,payload,header):
    response = requests.post(setting_up_baseurl+"login",data=payload,headers=header)
    assert response.status_code == 200