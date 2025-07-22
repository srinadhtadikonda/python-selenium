from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")
print("Title:", driver.title)
print("URL:", driver.current_url)
