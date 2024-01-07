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

# Test pour vérifier si la prédiction fonctionne
def test_make_prediction(trained_model):
    # Entrée de test pour la prédiction
    input_data = pd.read_csv('File_Data_Volume/atp_data.csv', sep=',')

    # Assurez-vous que la fonction make_prediction renvoie une sortie attendue
    output = trained_model.predict(input_data)

    # Vérifie si la sortie réelle correspond à la sortie attendue
    assert output is not None