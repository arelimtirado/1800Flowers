# Areli Tirado
# 04-11-2022
# Test 1800flowers for small text edits & functionality 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/arelitirado/QA/chromedriver")
driver.get("https://www.1800flowers.com/")
assert "Send Flowers & Exclusive Gifts" in driver.page_source
imgs = driver.find_elements(By.CSS_SELECTOR, '#appshell-container img')
assert len(imgs) == 46 
assert "Most Popular Flower Type" in driver.page_source
driver.close()