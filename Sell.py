import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# Credential valid
email      = "selenium@io.fga"
passw      = "FGAQA1"

# Data Produk
namabrg1 = "Testing By Selenium Automation"
namabrg2 = "Testing By Selenium Automation2"
namabrg3 = "Testing By Selenium Automation3"

harga1 = "99999"
harga2 = "88888"
harga3 = "-77777"

deskripsi1 = "Barang ini dijual menggunakan selenium automation FGA QA1"
deskripsi2 = "Barang ini dijual menggunakan selenium automation FGA QA1"
deskripsi3 = "Barang ini dijual menggunakan selenium automation FGA QA1"

class sell1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sell(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)

        # TC.Log.002.001
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(passw)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Jual']").click()
        time.sleep(2)

        # input data produk
        driver.find_element(By.XPATH, "//input[@id='product_name']").send_keys(namabrg1)
        driver.find_element(By.XPATH, "//input[@id='product_price']").send_keys(harga1)
        kategori = Select(driver.find_element(By.XPATH, "//select[@id='product_category_id']"))
        kategori.select_by_value("1")
        driver.find_element(By.XPATH, "//textarea[@id='product_description']").send_keys(deskripsi1)
        time.sleep(2)
        # Upload picture
        driver.find_element(By.XPATH, "/html/body/section/section/section/div/form/div[5]/div").click()
        time.sleep(3)
        pyautogui.write(r"D:\pict1.png")
        pyautogui.press("enter")
        time.sleep(2)
        # Terbitkan
        simpan = driver.find_element(By.XPATH,"//label[@for='product_status_published']")
        driver.execute_script("arguments[0].click();", simpan)
        driver.get_screenshot_as_file("TC.Sel.004.001.png")
        time.sleep(3)
        driver.close()

time.sleep(3)


class sell2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sell(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)

        # TC.Log.002.001
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(passw)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Jual']").click()
        time.sleep(2)

        # input data produk
        driver.find_element(By.XPATH, "//input[@id='product_name']").send_keys(namabrg2)
        driver.find_element(By.XPATH, "//input[@id='product_price']").send_keys(harga2)
        kategori = Select(driver.find_element(By.XPATH, "//select[@id='product_category_id']"))
        kategori.select_by_value("1")
        driver.find_element(By.XPATH, "//textarea[@id='product_description']").send_keys(deskripsi2)
        time.sleep(2)

        # Upload picture
        driver.find_element(By.XPATH, "/html/body/section/section/section/div/form/div[5]/div").click()
        time.sleep(3)
        pyautogui.write(r"D:\pict2.png")
        pyautogui.press("enter")
        time.sleep(3)
        # Preview
        prev = driver.find_element(By.XPATH, "//label[normalize-space()='Preview']")
        driver.execute_script("arguments[0].click();", prev)
        time.sleep(2)
        driver.get_screenshot_as_file("TC.Sel.004.002.png")

        # Terbitkan
        simpan = driver.find_element(By.XPATH, "//input[@name='commit']")
        driver.execute_script("arguments[0].click();", simpan)
        time.sleep(3)
        driver.close()

time.sleep(3)


class sell3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sell(self):
        driver = self.driver
        driver.maximize_window()

        # Precondition
        driver.get("https://secondhand.binaracademy.org/users/sign_in")
        time.sleep(2)

        # TC.Log.002.001
        driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(passw)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Jual']").click()
        time.sleep(2)

        # input data produk
        driver.find_element(By.XPATH, "//input[@id='product_name']").send_keys(namabrg3)
        driver.find_element(By.XPATH, "//input[@id='product_price']").send_keys(harga3)
        kategori = Select(driver.find_element(By.XPATH, "//select[@id='product_category_id']"))
        kategori.select_by_value("1")
        driver.find_element(By.XPATH, "//textarea[@id='product_description']").send_keys(deskripsi3)
        time.sleep(2)

        # Upload picture
        driver.find_element(By.XPATH, "/html/body/section/section/section/div/form/div[5]/div").click()
        time.sleep(3)
        pyautogui.write(r"D:\pict3.png")
        pyautogui.press("enter")
        time.sleep(3)
        # Terbitkan
        simpan = driver.find_element(By.XPATH, "//label[@for='product_status_published']")
        driver.execute_script("arguments[0].click();", simpan)

        harga_asli = driver.find_element(By.XPATH,"//p[@class='card-text fs-5']").text
        harga = harga_asli.replace('Rp ', '')
        harga = float(harga)

        driver.get_screenshot_as_file("TC.Sel.004.003.png")
        time.sleep(3)

        try:
            if harga < 1:
                print("Harga minus atau kurang dari 1")
        except:
            print("Tidak error")

        driver.close()


time.sleep(3)

if __name__  == '__main__':
    unittest.main()