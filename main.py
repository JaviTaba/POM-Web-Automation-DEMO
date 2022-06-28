from selenium import webdriver
from tests.demo_undostres import DemoUnDosTres


def main():
    #le pasamos el test que queremos probar
    demo = DemoUnDosTres()
    #Test
    demo.ejecutar_prueba()
if __name__ == "__main__":
    main()