table1.html

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>demo</title>
</head>
<body>
<table border="2">
<tr><td>eno</td><td>ename</td><td>esal</td><td>egrade</td></tr>
<tr><td>101</td><td>raghu</td><td>4500</td><td>A</td></tr>
<tr><td>102</td><td>vinay</td><td>5300</td><td>B</td></tr>
</table>
</body>
</html>




from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///D:/mycode/python-selenium/htmlfiles/table1.html")
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text for col in cols]
    print(" | ".join(data))


