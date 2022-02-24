import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones
from Funciones.Funciones import Funciones_Globales

tie = .2
def setup_function(function):
    print("\nInicia Test")
    global driver, func
    driver = webdriver.Chrome(executable_path="C:/driverchrome/chromedriver.exe")

    func = Funciones_Globales(driver)
    func.navegar("https://portalmx.infonavit.org.mx/wps/portal/infonavit.web/trabajadores/", tie)
    #func.navegar("https://micuenta.infonavit.org.mx/wps/portal/mci2/login/", tie)
    driver.maximize_window()

def teardown_function(function):
    print("Finaliza Test")
    driver.close()

def test_Login1():

    qcredito = driver.find_element_by_xpath("(//a[@href='?uri=nm:oid:Z6_2800GB01NG8H80AFEIE9L32GP1']"
                                            "[contains(.,'Quiero un crédito')])[2]")
    act = ActionChains(driver)
    act.move_to_element(qcredito).perform()

    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_6G00HC41N06TC0AFJQ0MOG2040']"
                         "[contains(.,'Quiero comprar')])[2]",5)
    driver.back()
    qcreditos = driver.find_element_by_xpath("(//a[@href='?uri=nm:oid:Z6_2800GB01NG8H80AFEIE9L32GP1']"
                                             "[contains(.,'Quiero un crédito')])[2]")
    act1 = ActionChains(driver)
    act1.move_to_element(qcreditos).perform()
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_6G00HC41N06TC0AFJQ0MOG2041']"
                         "[contains(.,'Quiero construir')])[2]",3)
    driver.back()
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_2800GB01NG8H80AFEIE9L32G50'][contains(.,'Tengo un crédito')])[2]"
                         ,tie)
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_2800GB01NG8H80AFEIE9L32GP0'][contains(.,'Mi ahorro')])[2]",tie)
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_2800GB01NG8H80AFEIE9L32G51']"
                         "[contains(.,'Retiro de mi ahorro')])[2]",tie)
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_6G00HC41N8IV70QE64O77R0Q80']"
                         "[contains(.,'Unamos Creditos')])[2]",tie)
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_6G00HC41NGRC30QPT19GUQ0K77'][contains(.,'ConstruYO')])[2]",tie)
    func.click_xpath_val("(//a[@href='?uri=nm:oid:Z6_6G00HC41N06TC0AFJQ0MOG2001']"
                         "[contains(.,'Centro de ayuda')])[2]",tie)

    driver.back()

if __name__ == '__main__':
    unittest.main()