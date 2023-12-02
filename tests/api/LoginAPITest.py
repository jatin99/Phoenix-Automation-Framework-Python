

# Assuming MyAPIUtil is the module, and APIUtil is the class within that module
from APIUtilsF.MyAPIUtil import APIUtil

headers = {
    # Your headers here
}

payload = {
    "username": "iamfd",
    "password": "password"
}

def test_login_api_request():
    # Assuming make_post_request is a method within the APIUtil class
    response = APIUtil.make_post_request("login", payload, headers)
    print(response.status_code)
    print(response.json())

# Call the function to test the login API request
test_login_api_request()
