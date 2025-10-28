import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f'Response is: {r.text}')


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers
    # print(f'Response Body is: {r.json()}')
    # print(f'Response Headers are: {r.headers}')
    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert r.headers['Server'] == 'github.com'

@pytest.mark.http
def test_not_found_request():
    r = requests.get('https://api.github.com/users/defunkt1233412')
    body = r.json()
    headers = r.headers

    assert body['message'] == 'Not Found'
    assert r.status_code == 404
    assert r.headers['Server'] == 'github.com'
