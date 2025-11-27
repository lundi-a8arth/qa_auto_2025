import pytest


@pytest.mark.ui
def test_check_login_positive(login_page):
    login_page.go_to()
    login_page.try_login("student", "Password123")
    assert (
        login_page.check_title() == "Logged In Successfully | Practice Test Automation"
    )


@pytest.mark.ui
def test_check_login_wrong_username(login_page):
    login_page.go_to()
    login_page.try_login("wrong_username", "Password123")
    assert login_page.element_by_id_visible("error")
    assert login_page.get_element_text_by_id("error") == "Your username is invalid!"


@pytest.mark.ui
def test_check_login_wrong_password(login_page):
    login_page.go_to()
    login_page.try_login("student", "wrongpassword")
    assert login_page.element_by_id_visible("error")
    assert login_page.get_element_text_by_id("error") == "Your password is invalid!"


@pytest.mark.ui
def test_check_logout(login_page):
    login_page.go_to()
    login_page.try_login("student", "Password123")
    assert (
        login_page.check_title() == "Logged In Successfully | Practice Test Automation"
    )
    login_page.click_logout()
    assert login_page.check_title() == "Test Login | Practice Test Automation"
