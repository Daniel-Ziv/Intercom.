from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def setup(driver):

        driver.get("url-of-admin-login-page")
        content = driver.find_element(By.XPATH, 'XPATH')
        content.click()
        user = driver.find_element(By.XPATH,'XPATH')
        user.send_keys('xxx')
        submit = driver.find_element(By.XPATH,'XPATH')
        submit.click()
        time.sleep(2)
        elementpass = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.XPATH, "XPATH")))
        time.sleep(1)
        passs = driver.find_element(By.XPATH,'XPATH')
        passs.send_keys('xxx')
        passubmit = driver.find_element(By.XPATH,'XPATH')
        passubmit.click()
        element = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, 'XPATH')))
        blackclick = driver.find_element(By.XPATH,'XPATH').click()