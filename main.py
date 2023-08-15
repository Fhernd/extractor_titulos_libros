from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://chat.openai.com/auth/login')

time.sleep(3)

try:
    # Encuentra el botón que tiene un div (hijo) con las clases "flex w-full gap-2 items-center justify-center" y el texto 'Log in':
    login_button = driver.find_element(By.XPATH, "//button[div[contains(@class, 'flex w-full gap-2 items-center justify-center') and text()='Log in']]")

    # Click en el botón de login:
    login_button.click()
except:
    print('No se pudo encontrar el botón de login')
    
    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'relative flex h-12 items-center justify-center rounded-md text-center text-base font-medium bg-[#3C46FF] text-[#fff] hover:bg-[#0000FF]')]")
    
    login_button.click()


time.sleep(3)

# Encuentra el campo que tiene el name 'username' y escribe esta cadena: 'will.i.am@mail.co':
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys('will.i.am@mail.co')

# Ahora presiona el botón de tipo 'submit' y que tiene el texto 'Continue':
submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Continue']")
submit_button.click()

# Espera 3 segundos:
time.sleep(2)

# Encuentra el input que tiene name "password" y escribe esta cadena: "12345678":
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('12345678')

time.sleep(2)

# Encuentra el botón de tipo 'submit' y que tiene el texto 'Continue':
submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Continue']")

submit_button.click()

time.sleep(100)
