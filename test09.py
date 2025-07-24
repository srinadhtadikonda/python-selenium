from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///D:/mycode/python-selenium/htmlfiles/table1.html")
cell = driver.find_element(By.XPATH, "//table/tbody/tr[3]/td[2]")
print("Data in 3rd row 2nd column:", cell.text)
