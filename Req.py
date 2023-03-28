import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# credential
username   = "debifrezz#3547"
email      = "selenium@io.fga"
password   = "FGAQA1"

class Req1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_regis(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/")
        
        # TC.Reg.001.001
        driver.find_element(By.PARTIAL_LINK_TEXT, "Masuk").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Daftar di sini").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys(username)
        driver.find_element(By.XPATH,"//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH,"//input[@id='user_password']").send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@name='commit']").click()
        driver.get_screenshot_as_file("TC.Reg.001.001.png")
        time.sleep(5)
        driver.close()

class Req2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_regis(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/")
        
        # TC.Reg.001.002
        driver.find_element(By.PARTIAL_LINK_TEXT, "Masuk").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Daftar di sini").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@name='commit']").click()
        time.sleep(5)
        driver.get_screenshot_as_file("TC.Reg.001.002.png")
        try:
            if driver.find_element(By.XPATH, "//input[@id='user_name']").get_attribute("validationMessage"):
                print("Harap isi bidang kosong")
                driver.close()
        except:
            driver.close()

class Req3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_regis(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/")
        
        # TC.Reg.001.003
        driver.find_element(By.PARTIAL_LINK_TEXT, "Masuk").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Daftar di sini").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys(username)
        driver.find_element(By.XPATH,"//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH,"//input[@id='user_password']").send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@name='commit']").click()
        time.sleep(5)
        driver.get_screenshot_as_file("TC.Reg.001.003.png")        

        try:
            if driver.find_element(By.XPATH,"//div[@class='form-text text-danger']").is_displayed():
                print("Email has already been taken")
                driver.close()
        except:
            driver.close()
        

if __name__ == '__main__':
    unittest.main()