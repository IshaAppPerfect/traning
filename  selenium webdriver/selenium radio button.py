from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')



radio_button = driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label')


radio_button.click()

time.sleep(1)
driver.quit()
