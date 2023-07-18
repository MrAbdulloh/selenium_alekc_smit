from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
                # uchta usernameni qo'shish
logins = ['standard_user', 'problem_user', 'performance_glitch_user']
random_login = random.choice(logins)

input_username = driver.find_element(By.ID, 'user-name')
input_username.send_keys(logins)
print('Input Login')
time.sleep(5)

input_password = driver.find_element(By.ID, 'password')
input_password.send_keys('secret_sauce')
print('Input Password')

input_password.send_keys(Keys.ENTER)

print("Click Login")
time.sleep(5)