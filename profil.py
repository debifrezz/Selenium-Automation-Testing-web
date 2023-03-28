import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Credential valid
email      = "selenium@io.fga"
passw      = "FGAQA1"

# Profile
alamat = "Jakarta Indonesia"
nohp = "18045"


class prof(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_profile(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)
        
        # Profile
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(passw)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/nav/div/div/div/ul/li[6]/a").click()
        driver.find_element(By.XPATH, "/html/body/nav/div/div/div/ul/li[6]/ul/li[1]/a/div/div").click()
        time.sleep(2)

        # Upload foto
        try:
            if driver.find_element(By.ID,"form-avatar-input").is_displayed():
                driver.find_element(By.ID,"form-avatar-input").click()
        except:
            print("ERROR")

        try:
            if driver.find_element(By.ID, "form-avatar-image").is_displayed():
                driver.find_element(By.ID, "form-avatar-image").click()
        except:
            pass

        time.sleep(1)
        pyautogui.write(r"D:\selenium.png")
        pyautogui.press("enter")
        # Isi data
        kategori = Select(driver.find_element(By.XPATH, "//select[@id='user_city_id']"))
        kategori.select_by_value("3")
        driver.find_element(By.XPATH, "//textarea[@id='user_address']").send_keys(alamat)
        driver.find_element(By.XPATH,"//input[@id='user_phone_number']").send_keys(nohp)
        time.sleep(2)
        driver.get_screenshot_as_file("TC.Prf.003.001.png") 
        simpan = driver.find_element(By.XPATH,"//input[@name='commit']")
        driver.execute_script("arguments[0].click();", simpan)
        time.sleep(3)
        driver.close()


if __name__ == '__main__':
    unittest.main()