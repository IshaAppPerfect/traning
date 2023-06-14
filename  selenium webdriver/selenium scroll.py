from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org")

driver.maximize_window()
#scroll by pixel
driver.execute_script("window.scrollBy(0,2000)","")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()
