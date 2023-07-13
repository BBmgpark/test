import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get('http://www.naver.com')

driver.maximize_window()

time.sleep(10)