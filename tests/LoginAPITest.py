 #Assuming MyAPIUtil is the module, and APIUtil is the class within that module
import sys
sys.path.append("C:/Users/Admin/Desktop/Batches/Phoenix-Automation-Framework-Python/")

from utils.APIUtil import APIUtil

headers = {
    # Your headers here
    "Authorization" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE3MDI4MDg3NzJ9.QzL9sFsnq3mvBMOZee6qISSfy6cRKNpbOTAMlNpwWNQ"
}

payload = {
    "username": "iamfd",
    "password": "password"
}
@pytest.mark.smoke
def test_login_api_request():
    # Assuming make_post_request is a method within the APIUtil class
    response = APIUtil.make_post_request("login", payload, headers)
    print(response.status_code)
    print(response.json())

    assert response.status_code == 201
    assert "Success" in response.text
    assert 'message' in response.text
    assert 'token' in response.text


    # Check specific values in the response
    #print(response.json()['data']['token'])

