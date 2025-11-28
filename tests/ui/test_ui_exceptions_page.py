from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    InvalidElementStateException,
    StaleElementReferenceException,
    TimeoutException,
)
import pytest


@pytest.mark.ui
def test_no_such_elem_exception(exceptions_page):
    exceptions_page.go_to()
    exceptions_page.press_add_btn()
    with pytest.raises(NoSuchElementException):
        exceptions_page.input_field_2_is_displayed_without_wait()


@pytest.mark.ui
def test_elem_not_interactable_exception(exceptions_page):
    exceptions_page.go_to()
    exceptions_page.press_add_btn()
    exceptions_page.send_text_to_input_field_2("Apple")
    with pytest.raises(ElementNotInteractableException):
        exceptions_page.press_save_bnt_by_name()


@pytest.mark.ui
def test_invalid_elem_state_exception(exceptions_page):
    exceptions_page.go_to()
    with pytest.raises(InvalidElementStateException):
        exceptions_page.clear_input_field_1()


@pytest.mark.ui
def test_stale_elem_reference_exception(exceptions_page):
    exceptions_page.go_to()
    element = exceptions_page.get_instructions_elem()
    assert element.is_displayed()
    exceptions_page.press_add_btn()
    with pytest.raises(StaleElementReferenceException):
        element.is_displayed()


@pytest.mark.ui
def test_timeout_exception(exceptions_page):
    exceptions_page.go_to()
    exceptions_page.press_add_btn()
    with pytest.raises(TimeoutException):
        exceptions_page.get_input_field_2_elem()
