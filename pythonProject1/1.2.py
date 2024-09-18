import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    time.sleep(2)
    driver.get("https://www.twitch.tv")
    time.sleep(5)
    textarea = driver.find_element(By.CSS_SELECTOR, "[placeholder='Поиск']")
    textarea.send_keys("voodosh")
    time.sleep(1)
    submit_button = driver.find_element(By.CSS_SELECTOR, "[icon='NavSearch']")
    submit_button.click()
    time.sleep(5)
finally:
    driver.quit()
