import json
from jsonschema import validate
import sys
sys.path.append("C:/Users/Admin/Desktop/Batches/Phoenix-Automation-Framework-Python/")

def test_schema_validation():
 
   

    # Construct the relative path to the schema file
    schema_file = "schema/createJobSchema.json"
    
    # Read the JSON schema from the file
    with open(schema_file, "r") as abc:
        expected_schema = json.load(abc)

    # Response body
    response_body = '{"message":"Job created successfully. ","data":{"id":28708,"mst_service_location_id":1,"mst_platform_id":2,"mst_warrenty_status_id":1,"mst_oem_id":1,"tr_customer_id":28725,"tr_customer_product_id":28715,"job_number":"JOB_28708"}}'

    # Parse response body as JSON
    response_data = json.load(response_body)

    # Perform schema validation
    try:
        validate(instance=response_data, schema=expected_schema)
    except Exception as e:
        assert False, f"Schema validation failed: {e}"

    # If validation passed, no assertion error will be raised
    assert True
