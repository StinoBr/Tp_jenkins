import sys, os
import pytest

# Ajouter la racine du projet au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app

@pytest.fixture
def client():
    application = app.app
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bienvenue" in response.data

def test_echo_success(client):
    payload = {"message": "Hello pipeline"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["echo"] == "Hello pipeline"

def test_echo_wrong_content_type(client):
    response = client.post("/echo", data="Hello")
    assert response.status_code == 415
    data = response.get_json()
    assert "error" in data
