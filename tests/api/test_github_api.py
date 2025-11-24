import pytest


@pytest.mark.api
def test_user_exists(github_api):
    status, user = github_api.get_user_by_username("defunkt")
    assert status == 200, f"Expected status code 200, got {status}"
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_non_exist_user(github_api):
    status, user = github_api.get_user_by_username("defunkt_user_nonexist")
    assert status == 404, f"Expected status code 404, got {status}"
    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    status, r = github_api.search_repo("become-qa-auto")
    assert status == 200, f"Expected status code 200, got {status}"
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    status, r = github_api.search_repo("lundi_a8arth_repository_non_exist")
    assert status == 200, f"Expected status code 200, got {status}"
    assert r["total_count"] == 0


@pytest.mark.api
def test_find_repo_with_single_char(github_api):
    status, r = github_api.search_repo("a")
    assert status == 200, f"Expected status code 200, got {status}"
    assert r["total_count"] != 0


@pytest.mark.api
def test_get_existing_commit_from_repo(github_api):
    status, r = github_api.get_commit_from_repo(
        "DmytroLunovAQA", "qa_auto_2025", "aabaf2a"
    )
    assert status == 200, f"Expected status code 200, got {status}"
    commit_message = r["commit"]["message"]
    assert "added github token" in commit_message


@pytest.mark.api
def test_get_non_existing_commit_from_repo(github_api):
    status, r = github_api.get_commit_from_repo(
        "DmytroLunovAQA", "qa_auto_2025", "not_exist"
    )
    assert status == 422, f"Expected status code 422, got {status}"
    commit_message = r["message"]
    assert "No commit found" in commit_message


@pytest.mark.api
def test_rate_limit_unauthorised(github_api_unauthorised):
    status, data = github_api_unauthorised.get_rate_limit()
    assert status == 200, f"Expected status code 200, got {status}"
    core_limit = data["resources"]["core"]["limit"]
    assert core_limit == 60, f"Expected 60, got {core_limit}"


@pytest.mark.api
def test_rate_limit_authorised(github_api):
    status, data = github_api.get_rate_limit()
    assert status == 200, f"Expected status code 200, got {status}"
    core_limit = data["resources"]["core"]["limit"]
    assert core_limit == 5000, f"Expected 5000, got {core_limit}"
