from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(LoginPage.URL)

    def try_login(self, username, password):
        login_element = self.driver.find_element(By.ID, "username")
        login_element.send_keys(username)
        password_element = self.driver.find_element(By.ID, "password")
        password_element.send_keys(password)
        button_element = self.driver.find_element(By.ID, "submit")
        button_element.click()

    def check_title(self):
        return self.driver.title
