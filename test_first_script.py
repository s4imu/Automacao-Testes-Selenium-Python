#It's necessary to work with selenium
import time
from selenium import webdriver

#It's necessary to work with the browser
browser = webdriver.Chrome()

browser.get("https://google.com") #access google.com
time.sleep(5)

