from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
# driver.maximize_window()

input_username = driver.find_element(By.ID, 'user-name')
input_username.send_keys('standard_users')
time.sleep(5)
    # backspace qilib delete qilad yani keyboard kati kor kadan baro'y 'Key' kati kor mekunan
input_username.send_keys(Keys.BACKSPACE)
time.sleep(5)

input_password = driver.find_element(By.ID, 'password')
input_password.send_keys('secret_sauce')

input_password.send_keys(Keys.ENTER)

filter = driver.find_element(By.CSS_SELECTOR, 'select[data-test="product_sort_container"]')
filter.send_keys(Keys.ENTER)
 # Keys.DOWN kati select a poyin kada TOP kati bolo kada mo'sho't
filter.send_keys(Keys.DOWN)
time.sleep(5)
filter.click()
time.sleep(5)
