import sys
import pytest
import requests
from BaseFixture.py import setBaseUrl
sys.path.append("C:/Users/Admin/Desktop/Batches/Phoenix-Automation-Framework-Python/")



# Fixture for payload
@pytest.fixture
def api_payload():
    return {
        "username": "iamfd",
        "password": "password"
    }


def test_login_api_request(setBaseUrl, api_headers, api_payload):
    # Act (Perform the action)
    response = requests.post(setBaseUrl+"/login", api_payload, api_headers)
    print(response.status_code)
    print(response.json())

    # Assert (Verify the outcome)
    assert response.status_code == 200
    assert "Success" in response.text
    assert 'message' in response.text
    assert 'token' in response.text

   
