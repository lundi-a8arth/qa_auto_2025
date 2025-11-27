from modules.ui.page_objects.login_page import LoginPage
import pytest


@pytest.mark.ui
def test_check_login_positive(login_page):
    login_page.go_to()
    login_page.try_login("student", "Password123")
    result = login_page.check_title
    print(result)
