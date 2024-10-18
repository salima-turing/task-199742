import pytest
from flask import Flask, jsonify
from my_streaming_app import app, process_data
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('my_streaming_app.process_data')
def test_process_data_endpoint(mock_process_data, client):
    # Mock the return value of process_data
    mock_process_data.return_value = {'result': 'success'}

    # Define the input data for the test
    input_data = {'key': 'value'}

    # Send a POST request to the /process endpoint with the input data
    response = client.post('/process', json=input_data)

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Assert that the response data matches the mocked return value
    assert response.json == {'result': 'success'}

    # Verify that the process_data function was called with the correct input
    mock_process_data.assert_called_once_with(input_data)
