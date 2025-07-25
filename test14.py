from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Firefox browser
driver = webdriver.Firefox()

# Open the local HTML file
driver.get("file:///D:/mycode/python-selenium/htmlfiles/checkbox.html")

# Wait for the page to load
time.sleep(1)

# Locate the checkboxes and text field
checkbox1 = driver.find_element(By.XPATH, "//input[@value='cream']")
checkbox2 = driver.find_element(By.XPATH, "//input[@value='sugar']")
order_textbox = driver.find_element(By.ID, "order")

# Step 1: Select checkbox1 (cream)
if not checkbox1.is_selected():
    checkbox1.click()
    print("Checked: cream")

# Wait for 2 seconds
time.sleep(2)

# Step 2: Select checkbox2 (sugar)
if not checkbox2.is_selected():
    checkbox2.click()
    print("Checked: sugar")

# Wait a moment for JavaScript onchange to update the order textbox
time.sleep(1)

# Step 3: Get and print the result from the text field
result = order_textbox.get_attribute("value")
print("Order TextBox Value:", result)

# Optional: Wait and close browser
time.sleep(3)
driver.quit()
