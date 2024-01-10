import requests
import pytest
import time

time.sleep(15)

# Remplacez l'URL par l'URL de votre API dans le conteneur
API_URL = "http://localhost:8000/home"

@pytest.mark.docker
def test_health_check():
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Health check failed with status code {response.status_code}"