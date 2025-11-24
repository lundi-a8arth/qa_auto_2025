import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user_by_username("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_non_exist_user(github_api):
    user = github_api.get_user_by_username("defunkt_user_nonexist")
    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("lundi_a8arth_repository_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_find_repo_with_single_char(github_api):
    r = github_api.search_repo("a")
    assert r["total_count"] != 0


@pytest.mark.api
def test_rate_limit_unauthorised(github_api_unauthorised):
    data = github_api_unauthorised.get_rate_limit()

    core_limit = data["resources"]["core"]["limit"]

    assert core_limit == 60, f"Expected 60, got {core_limit}"


@pytest.mark.api
def test_rate_limit_authorised(github_api):
    data = github_api.get_rate_limit()

    core_limit = data["resources"]["core"]["limit"]

    assert core_limit == 5000, f"Expected 5000, got {core_limit}"
