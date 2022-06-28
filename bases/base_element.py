from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    #Acciones que se pueden realizar en un elemento

    def find(self):
        element = WebDriverWait(
            driver=self.driver, timeout=20).until(
            EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def move_to(self):
        hover = ActionChains(self.driver).move_to_element(self.web_element)
        hover.perform()
