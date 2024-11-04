from fastapi.testclient import TestClient
from ..main import app
import pytest
from ..models import models
from ..controllers import order as order_controller

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_order(db_session):
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }
    order_object = models.Order(**order_data)
    created_order = order_controller.create(db_session, order_object)

    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.description == "Test order"