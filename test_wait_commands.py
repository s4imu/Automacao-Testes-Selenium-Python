from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# To work with conditions
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
# Using implicity wait
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/implicit-wait-example")
browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

# variable to work with the explicity wait requires the driver and timeout
wait = WebDriverWait(browser, 30)

# Waiting for a specific amount of time
time.sleep(2)

# Using implicity wait
checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()

# Using explicity wait

# finding an alert in the page
browser.find_element(By.ID, "alert").click()

# # wating until alery is displayed
wait.until(EC.alert_is_present())

# Checking if a text changes its content after an event
browser.find_element(By.ID, "populate-text").click()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text']"), "Selenium Webdriver"))
target_text = browser.find_element(By.XPATH, "//*[@class='target-text']").text
assert target_text == "Selenium Webdriver"

# Checking if a button is displayed after an event
browser.find_element(By.ID, "display-other-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))

# Checking if a button is enabled after an event
browser.find_element(By.ID, "enable-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "disable")))

# Checking if a checkbox will be checked after an event
checkbox = browser.find_element(By.ID, "ch")
browser.find_element(By.ID, "checkbox").click()
# requires an element as paramenter
wait.until(EC.element_to_be_selected(checkbox))

time.sleep(2)
