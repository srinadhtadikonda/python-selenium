<!DOCTYPE html>
<html>

<body>
  <p>How would you like your coffee?</p>
  <form>
    <input type="checkbox" name="coffee" value="cream" onchange="updateOrder()">With cream<br>
    <input type="checkbox" name="coffee" value="sugar" onchange="updateOrder()">With sugar<br>
    <input type="text" id="order" size="50">
  </form>

  <script>
    function updateOrder() {

      var x = document.getElementsByName('coffee');
      var y = Array.from(x).filter(checkbox => checkbox.checked);
      if (y.length > 0) 
{
        var z = y.map(checkbox => checkbox.value);
        document.getElementById('order').value = "You ordered coffee with " + z.join(', ');
      } 
else 
{
        document.getElementById('order').value = "";
      }
    }
  </script>
</body>

</html>


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("file:///D:/mycode/python-selenium/htmlfiles/checkbox.html")
checkbox = driver.find_element(By.XPATH, "//input[@value='cream']")
  # Wait for the page to load
# Check if not selected
if not checkbox.is_selected():
    time.sleep(1)
    checkbox.click()

