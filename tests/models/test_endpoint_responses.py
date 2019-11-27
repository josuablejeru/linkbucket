from flask import Flask
from app.routes import config_routes
import pytest
from flask_login import LoginManager


@pytest.fixture
def client_not_authorised():
    app = Flask(__name__)
    config_routes(app)
    login_manager = LoginManager(app=app)
    client = app.test_client()

    return client


def test_indexview_not_authorised(client_not_authorised):
    route = '/'
    response = client_not_authorised.get(route)
    assert response.status_code == 401
