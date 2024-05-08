from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the OrangeHRM login page
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Initialize Chrome WebDriver (make sure you have chromedriver installed and its path configured)
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Find the username field and enter username
username_locator = "txtUsername"
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, username_locator)))
username_field.send_keys("admin")

# Find the password field and enter password
password_locator = "txtPassword"
password_field = driver.find_element(By.ID, password_locator)
password_field.send_keys("admin123")

# Click the login button
login_button_locator = "btnLogin"
login_button = driver.find_element(By.ID, login_button_locator)
login_button.click()

# Wait until PIM module link is clickable and click it
pim_module_link_locator = "//a[@id='menu_pim_viewPimModule']"
pim_module_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pim_module_link_locator)))
pim_module_link.click()

# Click on an existing employee to delete
existing_employee_checkbox_locator = "//table[@id='resultTable']//tbody/tr[1]/td[1]/input"
existing_employee_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, existing_employee_checkbox_locator)))
existing_employee_checkbox.click()

# Click the Delete button
delete_button_locator = "btnDelete"
delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, delete_button_locator)))
delete_button.click()

# Confirm deletion
confirm_delete_button_locator = "dialogDeleteBtn"
confirm_delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, confirm_delete_button_locator)))
confirm_delete_button.click()

# Close the browser
driver.quit()
