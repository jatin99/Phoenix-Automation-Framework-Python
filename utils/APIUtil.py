import requests
class APIUtil:

    BASE_URL = "http://139.59.91.96:9000/v1/"

    def __init__(self):
        print("API UTIL")

    @staticmethod 
    def make_get_request(endpoint, headers):
        response = requests.get(APIUtil.BASE_URL+endpoint, headers = headers)
        return response

    @staticmethod 
    def make_post_request(endpoint, payload, headers):
       response =  requests.post(APIUtil.BASE_URL+endpoint, data=payload, headers=headers)
       return response