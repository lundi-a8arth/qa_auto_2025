from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TablePractice(BasePage):
    URL = "https://practicetestautomation.com/practice-test-table/"
    RADIO_LANG_ANY = (By.CSS_SELECTOR, "input[name='lang'][value='Any']")
    RADIO_LANG_JAVA = (By.CSS_SELECTOR, "input[name='lang'][value='Java']")
    RADIO_LANG_PYTHON = (By.CSS_SELECTOR, "input[name='lang'][value='Python']")
    CHECKBOX_LVL_BEGIN = (By.CSS_SELECTOR, "input[name='level'][value='Beginner']")
    CHECKBOX_LVL_INTERM = (By.CSS_SELECTOR, "input[name='level'][value='Intermediate']")
    CHECKBOX_LVL_ADVNC = (By.CSS_SELECTOR, "input[name='level'][value='Advanced']")
    DROPDOWN_ENROLL = (By.ID, "enrollDropdown")
    DROPDOWN_SORT = (By.ID, "sortBy")
    RESET_BUTTON = (By.ID, "resetFilters")
    NO_DATA_ELEMENT = (By.ID, "noData")
    TABLE_ROWS = (By.CSS_SELECTOR, "#courses_table tbody tr")

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(TablePractice.URL)

    def press_radio_button_lang_any(self):
        self.wait.until(
            EC.element_to_be_clickable((TablePractice.RADIO_LANG_ANY))
        ).click()

    def press_radio_button_lang_java(self):
        self.wait.until(
            EC.element_to_be_clickable((TablePractice.RADIO_LANG_JAVA))
        ).click()

    def press_radio_button_lang_python(self):
        self.wait.until(
            EC.element_to_be_clickable((TablePractice.RADIO_LANG_PYTHON))
        ).click()

    def checkbox_unselect_level_beginner(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((TablePractice.CHECKBOX_LVL_BEGIN))
        )
        if checkbox.is_selected():
            checkbox.click()

    def checkbox_unselect_level_intermediate(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((TablePractice.CHECKBOX_LVL_INTERM))
        )
        if checkbox.is_selected():
            checkbox.click()

    def checkbox_unselect_level_advanced(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((TablePractice.CHECKBOX_LVL_ADVNC))
        )
        if checkbox.is_selected():
            checkbox.click()

    def checkbox_select_level_beginner(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((TablePractice.CHECKBOX_LVL_BEGIN))
        )
        if not checkbox.is_selected():
            checkbox.click()

    def checkbox_select_level_intermediate(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((TablePractice.CHECKBOX_LVL_INTERM))
        )
        if not checkbox.is_selected():
            checkbox.click()

    def checkbox_select_level_advanced(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((TablePractice.CHECKBOX_LVL_ADVNC))
        )
        if not checkbox.is_selected():
            checkbox.click()

    def checkbox_set_all(self, checked: bool):
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[name='level']")

        for cb in checkboxes:
            if cb.is_selected() != checked:
                cb.click()

    def dropdown_enroll_pick(self, enroll_num):
        self.wait.until(
            EC.element_to_be_clickable((TablePractice.DROPDOWN_ENROLL))
        ).click()

        option_xpath = (
            By.XPATH,
            f"//ul[@class='dropdown-menu']/li[@data-value='{enroll_num}']",
        )
        self.wait.until(EC.element_to_be_clickable((option_xpath))).click()

    def dropdown_sort_pick(self, sort_by):
        select = Select(self.driver.find_element(*TablePractice.DROPDOWN_SORT))
        select.select_by_visible_text(sort_by)

    def get_visible_languages(self):
        rows = self.driver.find_elements(*TablePractice.TABLE_ROWS)
        visible_languages = []

        for row in rows:
            if row.is_displayed():
                cells = row.find_elements(By.TAG_NAME, "td")
                lang = cells[2].text.strip()
                visible_languages.append(lang)

        return visible_languages

    def get_visible_levels(self):
        rows = self.driver.find_elements(*TablePractice.TABLE_ROWS)
        visible_levels = []

        for row in rows:
            if row.is_displayed():
                cells = row.find_elements(By.TAG_NAME, "td")
                level = cells[3].text.strip()
                visible_levels.append(level)

        return visible_levels

    def get_visible_enrollments(self):
        rows = self.driver.find_elements(*TablePractice.TABLE_ROWS)
        visible_enrollments = []

        for row in rows:
            if row.is_displayed():
                cells = row.find_elements(By.TAG_NAME, "td")
                enrollments = cells[4].text.strip()
                visible_enrollments.append(int(enrollments))

        return visible_enrollments

    def get_no_data_element(self):
        no_data_element = self.wait.until(
            EC.visibility_of_element_located(TablePractice.NO_DATA_ELEMENT)
        )
        return no_data_element

    def get_reset_btn(self):
        reset_btn = self.wait.until(
            EC.visibility_of_element_located(TablePractice.RESET_BUTTON)
        )
        return reset_btn

    def press_reset_btn(self):
        self.wait.until(EC.element_to_be_clickable(TablePractice.RESET_BUTTON)).click()

    def get_selected_language(self):
        selected_lang = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name='lang']:checked")
            )
        )
        return selected_lang.get_attribute("value")

    def get_checked_levels(self):
        checkboxes = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "input[name='level']")
            )
        )
        return [cb.get_attribute("value") for cb in checkboxes if cb.is_selected()]

    def get_enrollments_option(self):
        enroll_option = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#enrollDropdown .dropdown-label")
            )
        )
        return enroll_option.text.strip()

    def check_reset_btn_is_invisible(self):
        return self.wait.until(
            EC.invisibility_of_element_located(TablePractice.RESET_BUTTON)
        )

    def check_all_rows_visible(self):
        rows = self.driver.find_elements(*TablePractice.TABLE_ROWS)
        return all(row.is_displayed() for row in rows)

    def get_visible_rows(self):
        all_rows = self.wait.until(
            EC.visibility_of_all_elements_located((TablePractice.TABLE_ROWS))
        )
        return [row for row in all_rows if row.is_displayed()]

    def get_enrollments_values(self):
        visible_rows = self.get_visible_rows()
        enrollments = []

        for row in visible_rows:
            cell = row.find_element(By.CSS_SELECTOR, "td[data-col='enrollments']")
            text = cell.text.strip()
            number = int(text.replace(",", ""))
            enrollments.append(number)

        return enrollments

    def get_course_name_values(self):
        visible_rows = self.get_visible_rows()
        course_names = []

        for row in visible_rows:
            cell = row.find_element(By.CSS_SELECTOR, "td[data-col='course']")
            text = cell.text.strip()
            course_names.append(text)

        return course_names
