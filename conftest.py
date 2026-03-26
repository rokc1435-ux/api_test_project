import pytest
from config.config import BASE_URL,PASSWORD,USERNAME
from api.api_client import ApiClient
@pytest.fixture(scope="session")
def client():
    c = ApiClient(BASE_URL)
    c.login(USERNAME, PASSWORD)
    return c
@pytest.fixture(scope="session")
def created_pet(client):
    pet_data = {"id": 456, "name": "fixdog", "status": "available"}
    response = client.post("/pet", json=pet_data)
    return response.json()
