from selenium import webdriver
import time

browser = webdriver.Chrome()

#maximize_window()
browser.maximize_window()

#get()
browser.get("https://google.com") #access the link in the parentheses
time.sleep(2)

#refresh()
browser.refresh() #refresh current page

#back()
browser.get("https://www.saucedemo.com/")
time.sleep(2)
browser.back() #return to the previous page

#forward()
time.sleep(2)
browser.forward()  #return to the next page

#creating a new tab
browser.switch_to.new_window("tab")
browser.get("https://wikipedia.com")
time.sleep(3)

#close()
browser.close() #closes a tab

#quit()
browser.switch_to.new_window("tab")
time.sleep(3)
browser.switch_to.new_window("tab")
time.sleep(3)
browser.quit()

time.sleep(3) #wait 5 seconds before close the windows
