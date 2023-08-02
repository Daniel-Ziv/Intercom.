from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def datagatherer(driver):
    df = pd.read_csv(r'csv_data/emlist.csv', encoding='iso-8859-1', on_bad_lines='skip', index_col=False)
    array = df['adir'].values
    print(array)

    date = time.strftime("%Y%m%d")

    reader = pd.read_csv(r'csv_data/emlist.csv', encoding='iso-8859-1', on_bad_lines='skip', index_col=False)
    emplo = reader['adir'].values
    csata = []
    frta = []
    ttca = []
    conva = []
    columns = ['name', 'csat', 'frt', 'ttc', 'convo']

    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, 'XPATH')))
    driver.get('url')


    for i in array:
        #setting up the pages by the employee name
        element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, 'XPATH')))
        clickcsat = driver.find_element(By.XPATH,'XPATH')
        clickcsat.click()
        searchbar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'XPATH')))
        searchbar.click()
        nameofemployee = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, 'XPATH')))
        nameofemployee.send_keys(i)
        time.sleep(0.5)
        nameofemployee.send_keys(Keys.ENTER)
        time.sleep(0.3)
        unfocus = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'XPATH')))
        unfocus.click()
        time.sleep(0.5)
        dateofdata = driver.find_element(By.XPATH,'XPATH')
        dateofdata.click()
        time.sleep(1)
        lastweekinfo = driver.find_element(By.XPATH, '/XPATH')
        lastweekinfo.click()
        time.sleep(1)
        csata.append(driver.find_element(By.XPATH,'XPATH').text.replace('or',''))
        print(csata)
        frtpage = driver.find_element(By.XPATH,'XPATH')
        frtpage.click()
        element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, 'XPATH')))
        frta.append(driver.find_element(By.XPATH,'XPATH').text)
        #ttc
        print(frta)
        ttca.append(driver.find_element(By.XPATH,'XPATH').text)
        convpage = driver.find_element(By.XPATH,'XPATH')
        convpage.click()
        print(ttca)
        element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, 'XPATH')))
        #כמות שיחות
        conva.append(driver.find_element(By.XPATH,'XPATH').text)
        print(conva)
        clickcsat.click()
        searchbar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'XPATH')))
        searchbar.click()
        nameofemployee = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'XPATH')))
        nameofemployee.send_keys(i)
        time.sleep(1)
        nameofemployee.send_keys(Keys.ENTER)
        time.sleep(1)
        unfocus = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'XPATH')))
        unfocus.click()
#now that we have finished gatharing the data into the array, we are converting it into a csv.


        dframe = pd.DataFrame(list(zip(emplo, csata, frta, ttca, conva)), columns=columns)
        print(dframe)
        name_of_file = '{}'.format(date)
        dframe.to_csv(r'csv_data/userdata.csv')
        the_file = dframe.to_csv(r'{}.csv'.format(name_of_file))