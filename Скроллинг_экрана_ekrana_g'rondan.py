import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.set_window_size(700 ,1000)

input_username = driver.find_element(By.ID, 'user-name')
input_username.send_keys('standard_user')
time.sleep(5)

input_password = driver.find_element(By.ID, 'password')
input_password.send_keys('secret_sauce')

input_password.send_keys(Keys.ENTER)
time.sleep(3)
    # X in x chap ros rafta mebiyot

    # X, Y ino hammesh px megirat yani px sel kati kor mekunat

    # Y boshat bolo poyin rafta mebiyot

# driver.execute_script("window.scrollTo(0, 900 )")          || in ba boshat xodomo megem 900 kun fufta


#  inash boshat to xodomo kuftagi elementda skrola meg'ironat

element = driver.find_element(By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[1]/a')
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView();", element)

time.sleep(3)
