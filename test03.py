from selenium import webdriver # type: ignore
driver = webdriver.Firefox()
driver.get("https://demo.guru99.com/test/newtours/")
expectedTitle = "Welcome: Mercury Tours"
actualTitle = driver.title
if expectedTitle == actualTitle:
    print("Test Passed")    
else:
    print("Test Failed")