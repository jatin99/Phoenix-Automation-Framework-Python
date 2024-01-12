import requests
import sys
import pytest

sys.path.append("C:/Users/Admin/Desktop/Batches/Phoenix-Automation-Framework-Python/")
from utils.APIUtil import APIUtil

def test_create_job_request():
    # Base URL
    base_url = "http://139.59.91.96:9000/v1/job/create"

    # Generate a random IMEI
    imei = APIUtil.generate_15_digit_random_number()

    # Headers for authorization
    headers = {
    "Authorization" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE3MDI4MDg3NzJ9.QzL9sFsnq3mvBMOZee6qISSfy6cRKNpbOTAMlNpwWNQ",
        "Content-Type": "application/json"
    }

    # Payload data
    payload = {
        "mst_service_location_id": 0,
        "mst_platform_id": 2,
        "mst_warrenty_status_id": 1,
        "mst_oem_id": 1,
        "customer": {
            "first_name": "Cornelius",
            "last_name": "Kuphal",
            "mobile_number": "0489568498",
            "mobile_number_alt": "",
            "email_id": "ned.mcglynn@yahoo.com",
            "email_id_alt": "jatinvsharma@gmail.com"
        },
        "customer_address": {
            "flat_number": "135",
            "apartment_name": "33166",
            "street_name": "9072 Marvin Point",
            "landmark": "9603",
            "area": "New Ashleyfort",
            "pincode": "6959689",
            "country": "Maharashtra",
            "state": "India"
        },
        "customer_product": {
            "dop": "2023-06-10T18:30:00.000Z",
            "serial_number": imei,
            "imei1": imei,
            "imei2": imei,
            "popurl": "2023-06-10T18:30:00.000Z",
            "product_id": 1,
            "mst_model_id": 1
        },
        "problems": [
            {
                "id": 1,
                "remark": "Phone not working"
            }
        ]
    }

    # Make the POST request
    response = requests.post(base_url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    # Assertions
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "Job created successfully" in response.json()["message"], "Unexpected message in response"
    assert "data" in response.json(), "Response does not contain 'data' field"

    


