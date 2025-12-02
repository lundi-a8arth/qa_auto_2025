from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ExceptionsPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-exceptions/"
    ADD_BTN_LOCATOR = (By.ID, "add_btn")
    EDIT_1_BTN = (By.CSS_SELECTOR, "#row1 .Edit")
    EDIT_2_BTN = (By.CSS_SELECTOR, "#row2 .Edit")
    SAVE_1_BTN = (By.CSS_SELECTOR, "#row1 .Save")
    SAVE_2_BTN = (By.CSS_SELECTOR, "#row2 .Save")
    REMOVE_BTN = (By.ID, "remove_btn")
    INPUT_FIELD_1 = (By.CSS_SELECTOR, "#row1 .input-field")
    INPUT_FIELD_2 = (By.CSS_SELECTOR, "#row2 .input-field")
    INSTRUCTIONS_ELEM = (By.ID, "instructions")

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(ExceptionsPage.URL)

    def press_add_btn(self):
        self.wait.until(
            EC.element_to_be_clickable((ExceptionsPage.ADD_BTN_LOCATOR))
        ).click()

    def press_edit_1_btn(self):
        self.wait.until(EC.element_to_be_clickable((ExceptionsPage.EDIT_1_BTN))).click()

    def press_edit_2_btn(self):
        self.wait.until(EC.element_to_be_clickable((ExceptionsPage.EDIT_2_BTN))).click()

    def press_save_1_btn(self):
        self.wait.until(EC.element_to_be_clickable((ExceptionsPage.SAVE_1_BTN))).click()

    def press_save_2_bnt(self):
        self.wait.until(EC.element_to_be_clickable((ExceptionsPage.SAVE_2_BTN))).click()

    def press_save_bnt_by_name(self):
        save_btn = self.driver.find_element(By.NAME, "Save")
        save_btn.click()

    def press_remove_btn(self):
        self.wait.until(EC.element_to_be_clickable((ExceptionsPage.REMOVE_BTN))).click()

    def send_text_to_input_field_1(self, text):
        self.wait.until(
            EC.visibility_of_element_located((ExceptionsPage.INPUT_FIELD_1))
        ).send_keys(text)

    def send_text_to_input_field_2(self, text):
        self.wait.until(
            EC.visibility_of_element_located((ExceptionsPage.INPUT_FIELD_2))
        ).send_keys(text)

    def clear_input_field_1(self):
        self.wait.until(
            EC.visibility_of_element_located((ExceptionsPage.INPUT_FIELD_1))
        ).clear()

    def clear_input_field_2(self):
        self.wait.until(
            EC.visibility_of_element_located((ExceptionsPage.INPUT_FIELD_2))
        ).clear()

    def input_field_2_is_displayed_without_wait(self):
        input_field_2 = self.driver.find_element(*ExceptionsPage.INPUT_FIELD_2)
        return input_field_2.is_displayed()

    def input_field_2_is_displayed_with_wait(self):
        input_field_2 = self.wait.until(
            EC.element_to_be_clickable((ExceptionsPage.INPUT_FIELD_2))
        )
        return input_field_2.is_displayed()

    def get_instructions_elem(self):
        instructions_elem = self.wait.until(
            EC.visibility_of_element_located((ExceptionsPage.INSTRUCTIONS_ELEM))
        )
        return instructions_elem

    def get_input_field_2_elem(self):
        input_field_2_elem = self.wait.until(
            EC.visibility_of_element_located((ExceptionsPage.INSTRUCTIONS_ELEM))
        )
        input_field_2_elem.is_displayed()
