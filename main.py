from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://chat.openai.com/')

time.sleep(5)

driver.find_element(By.XPATH, '//button[text()="Log in"]').click()

time.sleep(20)
