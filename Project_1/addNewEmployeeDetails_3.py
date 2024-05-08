from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# URL of the OrangeHRM site
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Admin credentials
admin_username = 'Admin'
admin_password = 'admin123'

# Initialize the WebDriver
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

    # Locate and click the Add button to add a new employee
    add_button_xpath = "//button[text()='Add']"
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_button_xpath))
    )
    add_button.click()

    # Fill in employee details
    first_name_input = driver.find_element(By.NAME, 'firstName')
    first_name_input.send_keys("Roja")

    middle_name_input = driver.find_element(By.NAME, 'middleName')
    middle_name_input.send_keys("Sir")

    last_name_input = driver.find_element(By.NAME, 'lastName')
    last_name_input.send_keys("K")

    employee_id_input = driver.find_element(By.CLASS_NAME, "oxd-input oxd-input--active")
    employee_id_input.send_keys("EMP001")

    # Click the Save button to save the employee details
    save_button_xpath = "//button[text()='Save']"
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, save_button_xpath))
    )
    save_button.click()

    print("Employee added successfully.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()