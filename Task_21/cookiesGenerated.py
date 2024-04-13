from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.saucedemo.com/")

# Capture cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

# Login
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Capture cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

# Log out
menu_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
menu_button.click()

# Wait until the logout link is clickable
logout_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
)
logout_link.click()

# Close the browser
driver.quit()

