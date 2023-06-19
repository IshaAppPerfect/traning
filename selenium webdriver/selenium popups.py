from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# driver.maximize_window()
location = "https://omayo.blogspot.com/"
driver.get(location)

#Click on the "Alert" button to generate the Simple Alert
button = driver.find_element(By.ID,'alert1')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )
# setting sleep time as 2 seconds---
time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

driver.close()
