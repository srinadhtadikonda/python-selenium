from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")
search_box = driver.find_element(By.NAME, "field-keywords")
search_box.send_keys("iphones")
search_box.submit()