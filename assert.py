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
input_password.send_keys('secret_sauce')

input_password.send_keys(Keys.ENTER)

time.sleep(5)
main_title = driver.find_element(By.CSS_SELECTOR, 'span[class=title]').text
    # assert korkadnash main_title budagi kati Products to'gri omdashtas mi anamuna test kadashtem assert kati
assert main_title == 'Products'
time.sleep(5)

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert url == get_url

