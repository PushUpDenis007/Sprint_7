import pytest
from helpers import create_user_payload, delete_courier_from_db
from api_client import CourierApi

@pytest.fixture
def courier_setup():

    payload=create_user_payload()
    CourierApi.create_courier(payload)
    yield payload
    delete_courier_from_db(payload)
