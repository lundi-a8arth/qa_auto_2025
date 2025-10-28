import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_non_exist_user(github_api):
    user = github_api.get_user('defunkt123nonexist')
    assert user['message'] == 'Not Found'

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert github_api.get_status_code == 200

