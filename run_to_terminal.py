from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # terminal baro'y Options a import kadan dakor
from selenium.webdriver.common.keys import Keys
import random
import time
        # chrome yala nakada terminala xudash kati run mekunat
chrome_option = Options()
chrome_option.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_option)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

    # to anamjaya code  nayistagi man

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
