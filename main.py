from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Si ChromeDriver no está en tu PATH, especifica su ubicación directamente
# driver = webdriver.Chrome(executable_path='/ruta/del/chromedriver')
driver = webdriver.Chrome()

# Navega hacia Google
driver.get("https://www.google.com")

# Encuentra la barra de búsqueda y escribe la consulta
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("¿Es Google hoy día, después de la aparición de ChatGPT, las nuevas páginas amarillas?")
search_box.send_keys(Keys.RETURN)  # Simula presionar "Enter"

# Esperar un poco
time.sleep(25)
