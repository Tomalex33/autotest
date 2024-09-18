from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import *
import os


def calc(x):
  return str(log(abs(12*sin(int(x)))))


link = "https://suninjuly.github.io/alert_accept.html"
link1 = 'https://suninjuly.github.io/redirect_accept.html'

try:
    # browser = webdriver.Chrome()
    # browser.get(link)
    # button = browser.find_element(By.CSS_SELECTOR, '.btn')
    # button.click()
    # time.sleep(2)
    # confirm = browser.switch_to.alert
    # confirm.accept()
    # time.sleep(2)
    # x_value = browser.find_element(By.ID, 'input_value')
    # x = x_value.text
    # total = calc(x)
    # answer = browser.find_element(By.ID, 'answer')
    # answer.send_keys(total)
    # button = browser.find_element(By.CSS_SELECTOR, '.btn')
    # button.click()

    browser = webdriver.Chrome()
    browser.get(link1)
    button = browser.find_element(By.CSS_SELECTOR, '.trollface')
    button.click()
    time.sleep(2)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)
    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    total = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(total)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
