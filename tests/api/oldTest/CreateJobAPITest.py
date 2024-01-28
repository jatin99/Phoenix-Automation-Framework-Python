import pytest
import requests
import sys

sys.path.append("C:/Users/Admin/Desktop/Batches/Phoenix-Automation-Framework-Python/")
from utils.APIUtil import APIUtil

# Fixture for base URL
@pytest.fixture
def base_url():
    return "http://139.59.91.96:9000/v1/job/create"

# Fixture for headers
@pytest.fixture
def api_headers():
    return {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....",  # Your actual token
        "Content-Type": "application/json"
    }

# Fixture for payload
@pytest.fixture
def api_payload():
    imei = APIUtil.generate_15_digit_random_number()

    return {
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

# Test using fixtures
def test_create_job_request(base_url, api_headers, api_payload):
    # Make the POST request
    response = requests.post(base_url, headers=api_headers, json=api_payload)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    # Assertions
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "Job created successfully" in response.json()["message"], "Unexpected message in response"
    assert "data" in response.json(), "Response does not contain 'data' field"
