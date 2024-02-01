from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from time import sleep
import sys

driver = webdriver.Chrome()
driver.get(
    "https://southeast-thisisourdomain.securerc.co.uk/onlineleasing/ourdomain-amsterdam-south-east/guestlogin.aspx?propleadsource_182801=portal"
)
# sleep(10)
username = driver.find_element(By.ID, "Username")
username.send_keys("arvanitopoulosmarios14@gmail.com")
password = driver.find_element(By.ID, "Password")
password.send_keys("bIvsyd-8cicfu-sagvaf")
sleep(10)
run = True
DISCONNECTED_MSG = (
    "Unable to evaluate script: disconnected: not connected to DevTools\n"
)
firstName = driver.find_element(By.ID, "txtName")
firstName.send_keys("Marios Ioannis")
lastName = driver.find_element(By.ID, "txtName2")
lastName.send_keys("Arvanitopoulos")
email = driver.find_element(By.ID, "txtEmail")
email.send_keys("arvanitopoulosmarios14@gmail.com")
phone = driver.find_element(By.ID, "txtPhone")
phone.send_keys("+31 6 41671751")
postal = driver.find_element(By.ID, "txtzipcode")
postal.send_keys("1104HJ")
message = driver.find_element(By.ID, "txtComments")
message.send_keys(
    "Hello my name is Marios, I am studying at VU for my masters in hydrology and I am looking for a place to stay for atleast the first year of my studies in Amsterdam"
)
# button_apply = driver.find_element(By.ID, "fakebuttondialog")
# button_apply.click()
while run:
    try:
        _ = driver.window_handles

    except InvalidSessionIdException:
        run = False
        break


sys.exit()
# Marios Ioannis
# Arvanitopoulos
# arvanitopoulosmarios14@gmail.com
# +31 6 41671751
# 1104HJ
# Hello my name is Marios, I am studying at VU for my masters in hydrology and I am looking for a place to stay for atleast the first year of my studies in Amsterdam
# bIvsyd-8cicfu-sagvaf
# 4305898629832008
# 12/25
# 958
