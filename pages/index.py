from selenium.webdriver.common.by import By
from bases.base_page import BasePage
from bases.locator import Locator
from bases.base_element import BaseElement


class Index(BasePage):

    url = 'https://sanbox.undostres.com.mx/index.php'


    #Elementos pertenecientes a la página

    @property
    def boton_recarga_celular(self):
        locator = Locator(by=By.CSS_SELECTOR, value="a[data-qa='mobile-tab']")
        return BaseElement(
                driver=self.driver,
                locator=locator)

    @property
    def input_operador(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='celular-operator']")
        return BaseElement(
            driver=self.driver,
            locator=locator)

    @property
    def operador_telcel(self):
        locator = Locator(by=By.CSS_SELECTOR, value="li[data-name='telcel']")
        return BaseElement(
            driver=self.driver,
            locator=locator)

    @property
    def nro_de_celular(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='celular-mobile']")
        return BaseElement(
            driver=self.driver,
            locator=locator)

    @property
    def monto_de_recarga(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[data-qa='celular-amount']")
        return BaseElement(
            driver=self.driver,
            locator=locator)

    @property
    def recarga_10_pesos(self):
        locator = Locator(by=By.CSS_SELECTOR, value="li[data-id='598']")
        return BaseElement(
            driver=self.driver,
            locator=locator)

    @property
    def boton_siguiente(self):
        locator = Locator(by=By.CSS_SELECTOR, value="button[data-qa='celular-pay']")
        return BaseElement(
            driver=self.driver,
            locator=locator)
