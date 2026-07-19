import pytest
import requests
from src.extract import fetch_data

def test_fetch_data_sucesso(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'results': [{'id': 'MLB123', 'price': 5000}]}
    mock_response.raise_for_status.return_value = None
    mocker.patch('requests.get', return_value=mock_response)
    
    data = fetch_data("iphone")
    assert len(data) == 1
    assert data[0]['id'] == 'MLB123'
