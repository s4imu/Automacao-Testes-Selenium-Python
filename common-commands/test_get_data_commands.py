from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

#Getting page title
title = browser.title
print(f'Page title is {title}')

#Getting page current url
current_url = browser.current_url
print(f'Page current URL is {current_url}')

#Getting page page source
page_source = browser.page_source
print(f'Page source is {page_source}')

browser.close()
