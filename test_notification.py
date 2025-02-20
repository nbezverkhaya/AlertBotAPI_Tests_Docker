import data
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

BASE_URL = config['DEFAULT']['BASE_URL']


def test_send_info_message():
    message = data.info

    response = requests.post(BASE_URL, json=message)

    assert response.status_code == 200
    assert response.json() == {'status': 'message acknowledged'}


def test_send_warning_message():
    message = data.warning

    response = requests.post(BASE_URL, json=message)

    assert response.status_code == 200
    assert response.json() == {'status': 'attempt to send message to chat successful'}


def test_send_bad_configured_message():
    message = data.bad_structure

    response = requests.post(BASE_URL, json=message)

    assert response.status_code == 422
