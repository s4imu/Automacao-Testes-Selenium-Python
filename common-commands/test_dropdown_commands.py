from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

# When working with dropdowns use Select

# Selecting by visible text
dropdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
dropdown_products.select_by_visible_text("Google")

# Selecting by value
dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("big baby cat")

# Selecting by index
dropdown_foods = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
for n in range(2):
    dropdown_foods.select_by_index(n)

time.sleep(3)