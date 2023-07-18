from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

logins = 'standard_user'

input_username = driver.find_element(By.ID, 'user-name')
input_username.send_keys(logins)
print('Input Login')

input_password = driver.find_element(By.ID, 'password')

 # .is_displayed() => in agar xato burond agar anamun vaqata xudashba proses a stop mekunat

assert input_password.is_displayed(), "Not  input password"

input_password.send_keys('secret_sauce')

input_password.send_keys(Keys.ENTER)

