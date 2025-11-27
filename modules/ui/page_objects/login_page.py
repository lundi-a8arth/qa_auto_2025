from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

    def click_logout(self):
        logout_btn = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )
        logout_btn.click()

    def check_title(self):
        return self.driver.title

    def element_by_id_visible(self, element_id):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, element_id)))
            return True
        except:
            return False

    def get_element_text_by_id(self, element_id):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, element_id)))
        return element.text
