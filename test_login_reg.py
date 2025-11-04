from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# URL correctas
URL_REGISTRO = "https://music-online-lilac.vercel.app/registro"
URL_SESION = "https://music-online-lilac.vercel.app/sesion"

# Datos de prueba
NOMBRE = "Usuario Testeo"
EMAIL = "usuariotest@duoc.cl"
PASSWORD = "1234"
DIRECCION = "Callebenyi 123"
REGION = "metropolitana"
COMUNA = "santiago"

# Cargar Chrome for Testing desde variable del workflow
chrome_path = os.getenv("CHROME_BINARY", "/opt/chrome/chrome")

options = Options()
options.binary_location = chrome_path
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Función para esperar elementos
def esperar(selector, by=By.CSS_SELECTOR, tiempo=10):
    return WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located((by, selector))
    )

try:
    print("🔵 TEST: Registro")
    driver.get(URL_REGISTRO)

    esperar("#nombre").send_keys(NOMBRE)
    esperar("#email").send_keys(EMAIL)
    esperar("#password").send_keys(PASSWORD)
    esperar("#confirmar").send_keys(PASSWORD)
    esperar("#direccion").send_keys(DIRECCION)

    # Seleccionar región
    esperar("select#region").click()
    esperar("select#region option[value='metropolitana']").click()

    time.sleep(0.3)

    # Seleccionar comuna
    esperar("select#comuna").click()
    esperar("select#comuna option[value='santiago']").click()

    # Enviar formulario
    esperar("button[type='submit']").click()

    # Validar toast
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "toast-body"),
            "Registro exitoso"
        )
    )

    print("✅ Registro exitoso en el test")

    time.sleep(1.5)

    # --- INICIO DE SESIÓN ---
    print("🔵 TEST: Login")

    driver.get(URL_SESION)
    time.sleep(1)

    # Esperar que realmente esté en la página correcta
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
    )

    campo_email = esperar("#email")
    campo_email.clear()
    campo_email.send_keys(EMAIL)

    campo_pass = esperar("#password")
    campo_pass.clear()
    campo_pass.send_keys(PASSWORD)

    # Click en iniciar 
    esperar("button[type='submit']").click()

    # Esperar mensaje de bienvenida
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "toast-body"),
            "Bienvenido"
        )
    )

    print("✅ Inicio de sesión: PASÓ correctamente")

except Exception as e:
    import traceback
    print("❌ Error en el test:")
    traceback.print_exc()

finally:
    time.sleep(1)
    driver.quit()
