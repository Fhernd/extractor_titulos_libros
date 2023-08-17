import os
import sqlite3
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

def obtener_credenciales():
    """
    Obtiene las credenciales de un archivo .env.

    Returns:
        EMAIL (str): Email de la cuenta de OpenAI.
        PASSWORD (str): Contraseña de la cuenta de OpenAI.
    """
    load_dotenv()

    EMAIL = os.environ.get('EMAIL')
    PASSWORD = os.environ.get('PASSWORD')

    return EMAIL, PASSWORD


def generar_driver():
    """
    Genera un driver de Selenium.

    Returns:
        driver (selenium.webdriver.chrome.webdriver.WebDriver): Driver de Selenium.
    """
    driver = webdriver.Chrome()

    return driver


def login(driver, email, password):
    """
    Inicia sesión en OpenAI.

    Args:
        driver (selenium.webdriver.chrome.webdriver.WebDriver): Driver de Selenium.
        email (str): Email de la cuenta de OpenAI.
        password (str): Contraseña de la cuenta de OpenAI.
    """
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
    username_field.send_keys(email)

    # Ahora presiona el botón de tipo 'submit' y que tiene el texto 'Continue':
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Continue']")
    submit_button.click()

    # Espera 3 segundos:
    time.sleep(1)

    # Encuentra el input que tiene name "password" y escribe esta cadena: "12345678":
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    time.sleep(1)


    # Encuentre el segundo button que tiene estas clases "btn relative btn-primary", se debe usar selectores CSS:
    btn_okay = driver.find_elements(By.CSS_SELECTOR, "button.btn.relative.btn-primary")
    btn_okay[1].click()

    time.sleep(1)

    # Encuentra el button con las clases "btn relative btn-neutral btn-small" y haz click en él:
    btn_dismiss = driver.find_element(By.CSS_SELECTOR, "button.btn.relative.btn-neutral.btn-small")
    btn_dismiss.click()

    time.sleep(1)

    # Encuentra con un selector CSS button.-my-1:
    btn_next = driver.find_element(By.CSS_SELECTOR, "button.-my-1")
    btn_next.click()


def hacer_prompt(driver, descripcion):
    """
    Hace un prompt en OpenAI.

    Args:
        driver (selenium.webdriver.chrome.webdriver.WebDriver): Driver de Selenium.
        descripcion (str): Descripción del prompt.
    """
    
    # Encontrar el textarea con el ID "prompt-textarea":
    prompt_textarea = driver.find_element(By.ID, "prompt-textarea")

    # Escribir el siguiente texto:
    prompt = f"""En el siguiente texto encuentra los títulos de libros: $$$ {descripcion} $$$ El formato de la salida debe ser el siguiente: Autor - Título del libro Por ejemplo: 1. Immanuel Kant - Crítica de la razón pura 2. Immanuel Kant - Crítica de la razón práctica 3. Immanuel Kant - Crítica del juicio
    """

    prompt_textarea.send_keys(prompt)

    # Presionar la tecla Return:
    prompt_textarea.send_keys(Keys.RETURN)

    time.sleep(5)

    # Verificar si existe un elemento con la clase "text-2xl":
    while True:
        try:
            driver.find_element(By.CLASS_NAME, "text-2xl")
        except:
            break

    try:
        # Extraer el último elemento que tiene las siguientes clases "markdown prose w-full break-words dark:prose-invert light":
        output = driver.find_elements(By.CSS_SELECTOR, "div.markdown.prose.w-full.break-words.dark\:prose-invert.light")[-1]

        if output:
            # Extrae el texto de cada uno de los elementos li que hay ahí dentro:
            libros = []
            for li in output.find_elements(By.TAG_NAME, "li"):
                print('libro: ', li.text)
                libros.append(li.text)
        else:
            return []
    except Exception as e:
        print('Error: ', e)
        return []


def conectar_bd(nombre_archivo):
    """
    Conecta a la base de datos.

    Args:
        nombre_archivo (str): Nombre del archivo de la base de datos.

    Returns:
        conn (sqlite3.Connection): Conexión a la base de datos.
        cursor (sqlite3.Cursor): Cursor de la base de datos.
    """
    conn = sqlite3.connect(nombre_archivo)
    cursor = conn.cursor()

    return conn, cursor


def obtener_episodios(conexion):
    """
    Obtiene los episodios de la base de datos.

    Args:
        conexion (sqlite3.Connection): Conexión a la base de datos.

    Returns:
        episodios (list): Lista de episodios.
    """
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM episodios")

    episodios = cursor.fetchall()

    return episodios



def main():
    EMAIL, PASSWORD = obtener_credenciales()

    driver = generar_driver()

    time.sleep(1)

    login(driver, EMAIL, PASSWORD)

    time.sleep(1000)


if __name__ == '__main__':
    main()
