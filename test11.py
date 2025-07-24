from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///D:/mycode/python-selenium/htmlfiles/table2.html")

# Locate the cell that contains 'SEVEN'
seven_cell = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]")
print(seven_cell.text)

driver.quit()
