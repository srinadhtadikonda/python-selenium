from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://demo.guru99.com/")
driver.find_element(By.NAME, "emailid").send_keys("srinadhtadikonda@gmail.com")
driver.find_element(By.NAME, "btnLogin").click()
