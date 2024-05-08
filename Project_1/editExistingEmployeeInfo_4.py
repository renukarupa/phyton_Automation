from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the OrangeHRM application
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Admin credentials
admin_username = 'Admin'
admin_password = 'admin123'

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

# Launch the URL
driver.get(url)

try:
    # Log in with admin credentials
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    driver.find_element(By.NAME, 'username').send_keys(admin_username)
    driver.find_element(By.NAME, 'password').send_keys(admin_password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)

    # Navigate to PIM module
    pim_menu_xpath = "//span[text()='PIM']"
    pim_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, pim_menu_xpath))
    )
    pim_menu.click()

    # Find and select the employee to edit
    employee_name = "Roja"
    # Adjust the XPath to match the structure of the employee list on the page
    employee_row_xpath = f"//div[@role='row']//div[text()='{employee_name}']"
    employee_row = driver.find_element(By.XPATH, employee_row_xpath)

    # Click the edit button within the employee row
    edit_button = employee_row.find_element(By.XPATH, ".//button[text()='Edit']")
    edit_button.click()

    # Edit the employee information
    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.clear()
    first_name_field.send_keys("Roja")

    middle_name_field = driver.find_element(By.NAME, 'middleName')
    middle_name_field.clear()
    middle_name_field.send_keys("Sir")

    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.clear()
    last_name_field.send_keys("K")

    employee_id_field = driver.find_element(By.CLASS_NAME, "oxd-input oxd-input--active")
    employee_id_field.clear()
    employee_id_field.send_keys("EMP001")

    # Save the changes
    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
    save_button.click()

finally:
    # Close the browser when done
    driver.quit()