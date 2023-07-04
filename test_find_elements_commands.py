from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

#find element
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

#inputing data in the inputs
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#find elements
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")

print(auth_fields)
print(len(auth_fields))

browser.close()