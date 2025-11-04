import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
        )
    
    # Відкриваємо сторінку
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке вводитимо неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, 'login_field')

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys('lundi-aBarth')

    # Знаходимо поле, в яке вводитимо неправильний пароль
    pass_elem = driver.find_element(By.ID, 'password')

    # Вводимо неправильний пароль
    pass_elem.send_keys('lundi-aBarth')

    # Знаходимо кнопку sign-in
    btn_elem = driver.find_element(By.NAME, 'commit')

    # Емулюємо натискання на кнопку sign-in
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо 
    assert driver.title == 'Sign in to GitHub · GitHub'

    # Закриваємо браузер
    driver.close()
