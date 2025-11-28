from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ExceptionsPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-exceptions/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(ExceptionsPage.URL)

    def press_add_btn(self):
        add_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "add_btn")))
        add_btn.click()

    def press_edit_1_btn(self):
        edit_1_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#row1 .Edit"))
        )
        edit_1_btn.click()

    def press_edit_2_btn(self):
        edit_2_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#row2 .Edit"))
        )
        edit_2_btn.click()

    def press_save_1_btn(self):
        save_1_btn = self.driver.find_element(By.CSS_SELECTOR, "#row1 .Save")
        save_1_btn.click()

    def press_save_2_bnt(self):
        save_2_btn = self.driver.find_element(By.CSS_SELECTOR, "#row2 .Save")
        save_2_btn.click()

    def press_save_bnt_by_name(self):
        save_btn = self.driver.find_element(By.NAME, "Save")
        save_btn.click()

    def press_remove_btn(self):
        remove_btn = self.driver.find_element(By.ID, "remove_btn")
        remove_btn.click()

    def send_text_to_input_field_1(self, text):
        input_field_1 = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#row1 .input-field"))
        )
        input_field_1.send_keys(text)

    def send_text_to_input_field_2(self, text):
        input_field_2 = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#row2 .input-field"))
        )
        input_field_2.send_keys(text)

    def clear_input_field_1(self):
        input_field_1 = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#row1 .input-field"))
        )
        input_field_1.clear()

    def clear_input_field_2(self):
        input_field_2 = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#row2 .input-field"))
        )
        input_field_2.clear()

    def input_field_2_is_displayed_without_wait(self):
        input_field_2 = self.driver.find_element(By.CSS_SELECTOR, "#row2 .input-field")
        return input_field_2.is_displayed()

    def input_field_2_is_displayed_with_wait(self):
        input_field_2 = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#row2 .input-field"))
        )
        return input_field_2.is_displayed()

    def get_instructions_elem(self):
        instructions_elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, "instructions"))
        )
        return instructions_elem

    def get_input_field_2_elem(self):
        input_field_2_elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, "instructions"))
        )
        input_field_2_elem.is_displayed()
