from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

input_username = driver.find_element(By.ID, 'user-name')
input_username.send_keys('standard_user')
time.sleep(5)

input_password = driver.find_element(By.ID, 'password')
input_password.send_keys('secret_sauce')
input_password.send_keys(Keys.ENTER)

time.sleep(5)