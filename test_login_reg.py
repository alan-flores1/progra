from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL_REGISTRO = "https://music-online-lilac.vercel.app/sesion"
URL_SESION = "https://music-online-lilac.vercel.app/registro"

NOMBRE = "Usuario Testeo"
EMAIL = "usuariotest@duoc.cl"
PASSWORD = "1234"
DIRECCION = "Callebenyi 123"
REGION = "metropolitana"
COMUNA = "Santiago"

driver = webdriver.Chrome()
driver.maximize_window()


def esperar(selector, by=By.CSS_SELECTOR, tiempo=10):
    return WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((by, selector)))


try:
    driver.get(URL_REGISTRO)

    esperar("#nombre").send_keys(NOMBRE)
    esperar("#email").send_keys(EMAIL)
    esperar("#password").send_keys(PASSWORD)
    esperar("#confirmar").send_keys(PASSWORD)
    esperar("#direccion").send_keys(DIRECCION)

    esperar("select#region").send_keys(REGION)

    time.sleep(0.5)

    esperar("select#comuna").send_keys(COMUNA)

    esperar("button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "toast-body"),
            "Registro exitoso"
        )
    )
    print("✅ Registro exitoso en el test")

    time.sleep(1.5)

    driver.get(URL_SESION)

    esperar("#email").send_keys(EMAIL)
    esperar("#password").send_keys(PASSWORD)

    esperar("button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "toast-body"),
            "Bienvenido"
        )
    )

    print("✅ Inicio de sesión: PASÓ correctamente")

except Exception as e:
    print("❌ Error en el test:", e)

finally:
    time.sleep(2)
    driver.quit()