from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import *
import os


def calc(x):
  return str(log(abs(12*sin(int(x)))))


link = "http://suninjuly.github.io/wait1.html"
link1 = "http://suninjuly.github.io/cats.html"
link2 = "http://suninjuly.github.io/wait2.html"
link3 = "https://suninjuly.github.io/explicit_wait2.html"

try:

    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link3)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element(By.ID, "book")
    button.click()
    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    total = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(total)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()

    # # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    # button.click()
    # message = browser.find_element(By.ID, "verify_message")
    #
    # assert "successful" in message.text


    # browser.find_element(By.ID, "button")

    # # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)
    #
    # browser.get(link)
    #
    # button = browser.find_element(By.ID, "verify")
    # button.click()
    # message = browser.find_element(By.ID, "verify_message")
    #
    # assert "successful" in message.text



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
