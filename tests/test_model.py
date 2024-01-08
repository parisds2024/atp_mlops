# tests/test_model.py

import joblib
import pytest
import pandas as pd

# Fixture pour charger le modèle
@pytest.fixture
def trained_model():
    # Remplacez "path/to/your_model.pkl" par le chemin réel vers votre modèle.pkl
    model = joblib.load("File_Data_Volume/atp_logistic_model.pkl")
    return model

# Test pour vérifier si le modèle charge correctement
def test_load_model(trained_model):
    assert trained_model is not None  # Vérifie que le modèle n'est pas None après le chargement