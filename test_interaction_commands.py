from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
login_button = browser.find_element(By.ID, "login-button")

# How to type in the inputs
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# How to click in the buttons
login_button.click()

# How to get the text data from the page elements
products_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(products_title.text)

# How to get the data from the attributes of the page elements
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("alt"))

browser.close()

