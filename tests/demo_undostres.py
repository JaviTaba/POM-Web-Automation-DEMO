import time
from pages.confirmation import Confirmation
from pages.index import Index
from pages.payment import Payment
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from bases.locator import Locator
from selenium import webdriver

class DemoUnDosTres:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.index = Index(driver=self.driver)
        self.payment = Payment(driver=self.driver)
        self.confirmation = Confirmation(driver=self.driver)
        self.wait = WebDriverWait(driver=self.driver, timeout=20)

    def solving_captcha(self):
        parent_windows = self.driver.window_handles
        print(parent_windows)
        iframe_locator = Locator(by=By.XPATH, value="//iframe[@title='reCAPTCHA']")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))
        self.payment.captcha_checkmark.click()
        self.driver.switch_to.default_content()


    def rellenar_datos_operador(self):
        self.index.go()
        self.index.input_operador.click()
        self.index.operador_telcel.click()
        self.index.nro_de_celular.input_text("8465433546")
        self.index.monto_de_recarga.click()
        self.index.recarga_10_pesos.click()
        self.index.boton_siguiente.click()


    def rellenar_metodo_de_pago(self):
        time.sleep(8)
        self.payment.boton_tarjeta_opciones.click()
        self.payment.boton_nueva_tarjeta.click()
        self.payment.input_nro_de_tarjeta.input_text("4111111111111111")
        self.payment.input_mes_exp.input_text("11")
        self.payment.input_anio_exp.input_text("25")
        self.payment.input_cvv.input_text("111")
        self.payment.input_email.input_text("test@test.com")
        self.payment.boton_pagar_con_tarjeta.click()
        self.payment.input_username.input_text("automationUDT1@gmail.com")
        self.payment.input_password.input_text("automationUDT123")
        self.solving_captcha()
        self.payment.boton_acceso.click()

    def confirmacion(self):
        time.sleep(8)
        assert (self.confirmation.recarga_exitosa.text == "¡Recarga Exitosa!")

    def ejecutar_prueba(self):
        self.rellenar_datos_operador()
        self.rellenar_metodo_de_pago()
        self.confirmacion()
        print("Tarea finalizada con éxito.")
