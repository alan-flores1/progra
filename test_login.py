from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL de tu aplicación (ajústala si es distinta)
URL = "https://tu-proyecto-en-codesandbox.io/sesion"

# Credenciales de prueba
USUARIO = "usuario_prueba"
PASSWORD = "123456"

# Iniciar navegador
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# Esperar a que cargue la página
time.sleep(2)

try:
    # Buscar los campos por su name, id o placeholder
    input_usuario = driver.find_element(By.NAME, "usuario")
    input_password = driver.find_element(By.NAME, "password")
    boton_login = driver.find_element(By.XPATH, "//button[contains(text(), 'Iniciar sesión')]")

    # Escribir datos
    input_usuario.send_keys(USUARIO)
    input_password.send_keys(PASSWORD)

    # Click en el botón
    boton_login.click()
    time.sleep(2)

    # Verificar si inicia sesión (por ejemplo, revisando un texto de bienvenida)
    assert "Bienvenido" in driver.page_source
    print("✅ Test de inicio de sesión: PASÓ correctamente")

except Exception as e:
    print("❌ Error en el test de inicio de sesión:", e)

finally:
    driver.quit()