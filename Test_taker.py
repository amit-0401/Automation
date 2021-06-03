from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class DMV_flow(unittest.TestCase):
    def test_taker(self):
        driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32\chromedriver.exe") #Chrome driver path
        #driver.get("https://chrome.google.com/webstore/detail/mvproctor/oohlbebhpgkiemcalbjdolaeopnhfblo")
        #time.sleep(5)
        #driver.find_element_by_partial_link_text("Add to Chrome").click()
        driver.get("https://dmv-uat.verificient.com/login")    #Website URL
        driver.maximize_window()
        print("URL-", driver.current_url)
        time.sleep(5)
        driver.find_element_by_name("username").send_keys(("amit+dmv_uat_student@verificient.com"))   #Email ID
        password=driver.find_element_by_name("password").send_keys("1234")   #Password
        driver.find_element_by_css_selector("button[type=submit]").click()   #Submit button click
        driver.implicitly_wait(10)
        time.sleep(10)
        #wait=WebDriverWait(driver,10)
        #plugin_dowload_button=driver.find_element_by_xpath("//translate[normalize-space()='Chrome plugin']")
        #d_element=wait.until(EC.presence_of_element_located((plugin_dowload_button)))
        #d_element.click()
        #driver.refresh()
        #driver.back()

        time.sleep(10)
        driver.find_element_by_link_text("Log Out").click()
        time.sleep(5)
        driver.close()


    if __name__=="__main__":
            test_taker(1)
            #unittest.main()
