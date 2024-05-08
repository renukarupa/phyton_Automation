from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# URL of the OrangeHRM login page
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get(url)

# Find the username field and enter correct username
username_locator = 'username'
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, username_locator)))
username_field = driver.find_element(By.NAME, username_locator)
username_field.send_keys("Admin")

# Find the password field and enter invalid password
password_locator = 'password'
#WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, password_locator)))
password_field = driver.find_element(By.NAME, password_locator)
password_field.send_keys("invalid password")

# Click the submit button
submit_button_locator = '//button[@type="submit"]'
#WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, submit_button_locator)))
submit_button = driver.find_element(By.XPATH, submit_button_locator)
submit_button.click()
sleep(3)

# Close the browser
driver.quit()

