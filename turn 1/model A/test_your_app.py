from flask import Flask, request, jsonify
import unittest
from unittest.mock import patch, Mock
import pytest
from your_app import app, process_data_task


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_process_data_task_valid_input(client):
    # Mock the data source and sink
    data_source_mock = Mock()
    data_sink_mock = Mock()

    # Define the expected input data and output
    input_data = [{"key": 1, "value": "a"}, {"key": 2, "value": "b"}]
    expected_output = [{"key": 1, "result": "processed a"}, {"key": 2, "result": "processed b"}]

    # Patch the data source and sink in the process_data_task function
    with patch('your_app.data_source', data_source_mock), patch('your_app.data_sink', data_sink_mock):
        data_source_mock.return_value = input_data

        # Call the process_data_task function
        process_data_task()

        # Assert that the data sink was called with the expected output
        data_sink_mock.assert_called_once_with(expected_output)


if __name__ == '__main__':
    pytest.main()
