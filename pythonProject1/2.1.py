from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

def calc(x):
  return str(log(abs(12*sin(int(x)))))

# link = "https://suninjuly.github.io/math.html"
link = "http://suninjuly.github.io/get_attribute.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#     answer = browser.find_element(By.ID, "answer")
#     answer.send_keys(y)
#     checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
#     checkbox.click()
#     radiobutton = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
#     radiobutton.click()
#     submit = browser.find_element(By.CSS_SELECTOR, '.btn')
#     submit.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    truser = browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')
    value = truser.get_attribute('valuex')
    total = calc(value)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(total)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    time.sleep(1)
    radiobtn = browser.find_element(By.ID, 'robotsRule')
    radiobtn.click()
    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
