from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/")

# Trying to login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
password = driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

# Checking if redirects to products page
assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()