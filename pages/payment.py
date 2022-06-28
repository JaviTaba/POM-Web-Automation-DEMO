from selenium.webdriver.common.by import By
from bases.base_page import BasePage
from bases.locator import Locator
from bases.base_element import BaseElement


class Payment(BasePage):

    url = 'https://sanbox.undostres.com.mx/payment.php'


    #Elementos pertenecientes a la página

    @property
    def boton_tarjeta_opciones(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[id='panel-title-card']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def boton_nueva_tarjeta(self):
        locator = Locator(by=By.CSS_SELECTOR, value="tr[id='radio-n']")
        return BaseElement(driver=self.driver,
                           locator= locator)

    @property
    def input_nro_de_tarjeta(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='numero-de-tarjeta-input']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def input_mes_exp(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='mes-input']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def input_anio_exp(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='expyear-input']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def input_cvv(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='cvv-input']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def input_email(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[type='email']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def boton_pagar_con_tarjeta(self):
        locator = Locator(by=By.CSS_SELECTOR, value="button[id='paylimit']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def input_username(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[id='usrname']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def input_password(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[id='psw']")
        return BaseElement(driver=self.driver,
                           locator=locator)


    @property
    def captcha_checkmark(self):
        locator = Locator(by=By.CSS_SELECTOR, value="span[role='checkbox']")
        return BaseElement(driver=self.driver,
                           locator=locator)

    @property
    def boton_acceso(self):
        locator = Locator(by=By.CSS_SELECTOR, value="button[id='loginBtn']")
        return BaseElement(driver=self.driver,
                           locator=locator)