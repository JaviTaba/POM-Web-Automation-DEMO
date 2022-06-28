from selenium.webdriver.common.by import By
from bases.base_page import BasePage
from bases.locator import Locator
from bases.base_element import BaseElement


class Confirmation(BasePage):

    url = 'https://sanbox.undostres.com.mx/index.php'

    #Texto de confirmación
    @property
    def recarga_exitosa(self):
        locator = Locator(by=By.XPATH, value="//div[@class='visual-message']")
        return BaseElement(
            driver=self.driver,
            locator=locator)