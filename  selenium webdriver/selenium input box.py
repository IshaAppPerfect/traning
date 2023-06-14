
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# select class name where is input box are present
element = driver.find_elements(By.CLASS_NAME, "text_field")

# find number of input box
print(len(element))

# fill value in input box
driver.find_element(By.XPATH,'//*[@id="RESULT_TextField-1"]').send_keys("ISHA")
driver.find_element(By.XPATH,'//*[@id="RESULT_TextField-2"]').send_keys("GUPTA")
driver.find_element(By.XPATH,'//*[@id="RESULT_TextField-3"]').send_keys("8787111FG1")

# check status
x = driver.find_element(By.XPATH,'//*[@id="RESULT_TextField-1"]').is_displayed()
print(x)
time.sleep(1)
driver.close()
