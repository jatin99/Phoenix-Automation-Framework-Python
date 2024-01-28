import sys
import pytest
sys.path.append("C:/Users/Admin/Desktop/Batches/Phoenix-Automation-Framework-Python/")

from utils.APIUtil import APIUtil

# Fixture for headers
@pytest.fixture
def api_headers():
    return {
    "Authorization" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE3MDI4MDg3NzJ9.QzL9sFsnq3mvBMOZee6qISSfy6cRKNpbOTAMlNpwWNQ"
    }

# Fixture for payload
@pytest.fixture
def api_payload():
    return {
        "username": "iamfd",
        "password": "password"
    }

# Fixture for APIUtil instance
@pytest.fixture
def api_util_instance():
    return APIUtil()

def test_login_api_request(api_util_instance, api_headers, api_payload):
    # Act (Perform the action)
    response = api_util_instance.make_post_request("login", api_payload, api_headers)
    print(response.status_code)
    print(response.json())

    # Assert (Verify the outcome)
    assert response.status_code == 200
    assert "Success" in response.text
    assert 'message' in response.text
    assert 'token' in response.text

   
