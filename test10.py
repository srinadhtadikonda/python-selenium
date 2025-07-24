
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="2">
        <tr><td>ONE</td><td>TWO</td></tr>
        <tr>
            <td>THREE</td>
            <td>
                <table border="1">
                    <tr><td>FOUR</td><td>FIVE</td></tr>
                    <tr><td>SIX</td><td>SEVEN</td></tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///D:/mycode/python-selenium/htmlfiles/table2.html")
inner_table = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[2]/table")
rows = inner_table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text for col in cols]
    print(" | ".join(data))
