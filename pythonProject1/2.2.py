from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import *
import os


def calc(x):
  return str(log(abs(12*sin(int(x)))))

link = "https://suninjuly.github.io/file_input.html"

# browser = webdriver.Chrome()
# browser.get(link)
# current_dir = os.path.abspath(os.path.dirname(__file__))
# print(current_dir)
# file_path = os.path.join(current_dir, 'file.txt')
# vvod = browser.find_element(By.ID, 'answer')
# vvod.send_keys(file_path)
# time.sleep(10)
# browser.quit()
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.ru")
    load = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    load.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     value = browser.find_element(By.ID, 'input_value')
#     x_value = value.text
#     total = calc(int(x_value))
#     vvod = browser.find_element(By.ID, 'answer')
#     vvod.send_keys(total)
#     checkbox = browser.find_element(By.ID, 'robotCheckbox')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
#     time.sleep(2)
#     checkbox.click()
#     radiobutton = browser.find_element(By.ID, 'robotsRule')
#     radiobutton.click()
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
#
#
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
