from unittest import mock
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #ill admit, i was having trouble with pathing, classic python

from app.random_user_loader import RandomUserLoader

@pytest.fixture
def random_user_loader():
    return RandomUserLoader()


def test_parse_user_json(random_user_loader):
    # Testing the _parse_user_json method with a sample user dictionary
    user_dict = {
        "name": {"first": "John", "last": "Doe"},
        "gender": "male",
        "email": "john.doe@example.com",
        "dob": {"date": "1990-01-01"},
        "phone": "123-456-7890",
        "nat": "US"
    }

    result = random_user_loader._parse_user_json(user_dict)

    assert result == {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "male",
        "email_address": "john.doe@example.com",
        "date_of_birth": "1990-01-01",
        "phone_number": "123-456-7890",
        "nationality": "US"
    }

@mock.patch('app.random_user_loader.RandomUserLoader._get_users_json')
def test_write_user_results_file(mock_get_users_json, random_user_loader, tmp_path):
    # Mock the _get_users_json method to return a list with a sample user dictionary
    mock_get_users_json.return_value = [
        {
            "name": {"first": "John", "last": "Doe"},
            "gender": "male",
            "email": "john.doe@example.com",
            "dob": {"date": "1990-01-01"},
            "phone": "123-456-7890",
            "nat": "US",
        }
    ]

    # Call the _write_user_results_file method with tmp_path as the base path
    url = 'https://example.com/api/users'
    random_user_loader._write_user_results_file(url, path='test/local_data')

    # Check if the file was created and contains expected content
    assert os.path.exists('test/local_data/user_information.json') == True

   