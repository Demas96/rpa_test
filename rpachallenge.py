import requests
import time

import pandas

from selenium import webdriver
from selenium.webdriver.common.by import By


url_download = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
response = requests.get(url_download)
with open('challenge.xlsx', 'wb') as file:
    file.write(response.content)
file = pandas.read_excel('challenge.xlsx')

driver = webdriver.Chrome()
driver.get('https://rpachallenge.com/')
driver.maximize_window()
start_button = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
submit_button = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
start_button.click()
for i, row in file.iterrows():
    d = {'First Name': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]'),
         'Last Name ': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]'),
         'Company Name': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]'),
         'Role in Company': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]'),
         'Address': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]'),
         'Email': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]'),
         'Phone Number': driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]'),
         }
    for index in row.index:
        d[index].send_keys(file[index][i]) if index != 'Phone Number' else d[index].send_keys(int(file[index][i]))
    submit_button.click()
time.sleep(5)
print('Success!')
