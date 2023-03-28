import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Credential valid
email      = "selenium@io.fga"
passw      = "FGAQA1"

# Credential invalid
email1 = "sel1@nu.i"
passw1 = "321"


class Log1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)

        # TC.Log.002.001
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH,"//input[@id='user_password']").send_keys(passw)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(2)
        driver.get_screenshot_as_file("TC.Log.002.001.png") 
        driver.close()

time.sleep(3)

class Log2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)

        # TC.Log.002.002
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email1)
        driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(passw1)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(2)

        driver.get_screenshot_as_file("TC.Log.002.002.png") 

        try:
            if driver.find_element(By.XPATH, "//div[@role='alert']").is_displayed():
                print("Invalid Email or password.")
                driver.close()
        except:
            driver.close()
        
time.sleep(3)

class Log3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)

        # TC.Log.002.003
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys("aa@a.com")
        driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys('123')
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='user_email']").clear()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='user_password']").clear()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(3)
        driver.get_screenshot_as_file("TC.Log.002.003.png") 
        
        try:
            if driver.find_element(By.XPATH, "//input[@id='user_email']").get_attribute("validationMessage"):
                print("Harap isi bidang kosong")
                driver.close()
        except:
            driver.close()

time.sleep(3)

if __name__ == '__main__':
    unittest.main()