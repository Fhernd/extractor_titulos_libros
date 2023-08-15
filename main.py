from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Si ChromeDriver no está en tu PATH, especifica su ubicación directamente
# driver = webdriver.Chrome(executable_path='/ruta/del/chromedriver')
driver = webdriver.Chrome()

# Navega hacia Google
driver.get("https://www.google.com")

# Encuentra la barra de búsqueda y escribe la consulta
search_box = driver.find_element_by_name("q")
search_box.send_keys("¿Es Google hoy día, después de la aparición de ChatGPT, las nuevas páginas amarillas?")
search_box.send_keys(Keys.RETURN)  # Simula presionar "Enter"

# Esperar un poco (esto es solo para que puedas ver el resultado; en producción, podrías omitir o reducir esta espera)
time.sleep(5)
time.sleep(60)

# Cierra el navegador
driver.quit()
