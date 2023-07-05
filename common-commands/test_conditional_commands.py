import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com")

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#checking if an element is displayed
username_displayed = username.is_displayed()
print(username_displayed)

#checking if an element is enabled
username_enabled = username.is_enabled()
print(username_enabled)

#checking if an element is enabled
checkbox_check = checkbox_remember_me.is_selected()
print(checkbox_check)

checkbox_remember_me.click() #command to click
time.sleep(3)
checkbox_check = checkbox_remember_me.is_selected()
print(checkbox_check)

browser.close()
