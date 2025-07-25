from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Firefox browser
driver = webdriver.Firefox()

# Open the local HTML file
driver.get("file:///D:/mycode/python-selenium/htmlfiles/checkbox.html")

# Wait for the page to load
time.sleep(1)

# Find checkbox1 (cream) and checkbox2 (sugar)
checkbox1 = driver.find_element(By.XPATH, "//input[@value='cream']")
checkbox2 = driver.find_element(By.XPATH, "//input[@value='sugar']")

# Step 1: Check checkbox1 (cream) if not already selected
if not checkbox1.is_selected():
    checkbox1.click()

# Step 2: Wait for 2 seconds
time.sleep(2)

# Step 3: Uncheck checkbox1 if it's selected
if checkbox1.is_selected():
    checkbox1.click()

# Step 4: Wait for 1 second
time.sleep(1)

# Step 5: Check checkbox2 (sugar) if not already selected
if not checkbox2.is_selected():
    checkbox2.click()

