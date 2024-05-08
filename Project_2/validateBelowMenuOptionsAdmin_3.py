from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

# URL of the OrangeHRM site
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Launch the URL
driver.get(url)

# Admin credentials
admin_username = 'Admin'
admin_password = 'admin123'

try:
    # Log in with admin credentials
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    driver.find_element(By.NAME, 'username').send_keys(admin_username)
    driver.find_element(By.NAME, 'password').send_keys(admin_password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)

    # Wait for the Admin page to load and verify it by looking for the side pane
    side_pane_xpath = "//ul[contains(@class, 'oxd-main-menu')]"
    side_pane = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, side_pane_xpath))
    )

    # Define the expected main menu options
    expected_options = [
        'Admin',
        'PIM',
        'Leave',
        'Time',
        'Recruitment',
        'My Info',
        'Performance',
        'Dashboard',
        'Directory',
        'Buzz',
        'Maintenance'
    ]

    # Loop through expected options and validate their presence
    for option in expected_options:
        option_found = False

        while True:
            try:
                # Re-fetch the side pane each iteration to avoid stale references
                side_pane = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, side_pane_xpath))
                )

                # Find all menu items within the side pane
                menu_items = side_pane.find_elements(By.TAG_NAME, 'li')

                # Iterate through menu items to find the expected option
                for item in menu_items:
                    menu_text = item.text.strip()

                    if menu_text == option:
                        print(f"{option} is present on the side pane.")
                        # Option found, mark it as found
                        option_found = True

                        # Use ActionChains to click on the menu item
                        actions = ActionChains(driver)
                        actions.move_to_element(item).click().perform()

                        print(f"Clicked on {option} and navigating through the sub-menu.")

                        # Break the inner loop since the option is found
                        break

                # If the option is found, break the loop
                if option_found:
                    break

            except StaleElementReferenceException:
                # Handle the exception by retrying the loop
                print(f"StaleElementReferenceException encountered. Retrying finding and clicking on {option}...")

        # If option was not found
        if not option_found:
            print(f"{option} is NOT present on the side pane.")

finally:
    # Close the WebDriver
    driver.quit()
