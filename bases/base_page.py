
class BasePage(object):

    url = None

    #Métodos comunes a todas las páginas

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
