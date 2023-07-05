from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']").is_displayed()

print("All tests passed!!!")
