import pytest

@pytest.fixture(scope="module")
def setBaseUrl():
    return "http://139.59.91.96:9000/v1"
