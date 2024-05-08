from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to the URL
    driver.get(url)

    # Allow the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'p'))
    )

    # Locate the `<p>` tag containing the "Forgot your password?" link using XPath
    forgot_password_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//p/a[text()="Forgot your password?"]'))
    )

    # Click the link
    forgot_password_link.click()

    # Allow time for the new page to load
    time.sleep(2)

    # Locate the username input field and validate its visibility
    username_input = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )

    # Enter the username
    username = 'Admin'
    username_input.send_keys(username)

    submit_button_locator = '//button[@type="submit"]'
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, submit_button_locator)))
    submit_button = driver.find_element(By.XPATH, submit_button_locator)
    submit_button.click()
    #sleep(3)

    # Allow time for the request to process
    time.sleep(2)

except Exception as e:
    # If any exception occurs, print the error message
    print("An error occurred:", e)

finally:
    # Close the WebDriver instance in the end
    driver.quit()
