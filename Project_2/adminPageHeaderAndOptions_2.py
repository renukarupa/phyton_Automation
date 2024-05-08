from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# URL of the OrangeHRM site
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

#Initialize Chrome WebDriver
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

    # Navigate to the Admin page
    admin_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Admin']"))
    )
    admin_tab.click()

    # Define the expected options
    expected_options = [
        'User Management',
        'Job',
        'Organization',
        'Qualifications',
        'Nationalities',
        'Configuration'
    ]

    # Locate the main menu element
    main_menu_xpath = "//ul[@class='oxd-main-menu']"
    main_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, main_menu_xpath))
    )

    # Locate all menu items within the main menu
    menu_items = main_menu.find_elements(By.TAG_NAME, 'li')

    # Keep track of found options
    found_options = set()

    # Iterate through menu items and validate their presence
    for item in menu_items:
        # Check each menu item's text against the expected options
        menu_text = item.text.strip()
        print(f"Checking menu item: {menu_text}")
        if menu_text in expected_options:
            found_options.add(menu_text)
            print(f"{menu_text} is present on the Admin page.")

            # Use ActionChains to click on the menu item
            actions = ActionChains(driver)
            actions.move_to_element(item).click().perform()

            # Add a brief wait time after clicking
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, main_menu_xpath))
            )

            print(f"Clicked on {menu_text} and navigating through sub-menu.")

        # Add delay if necessary
        driver.implicitly_wait(2)

    # Check for missing options
    missing_options = set(expected_options) - found_options
    for missing_option in missing_options:
        print(f"{missing_option} is NOT present on the Admin page.")

finally:
    # Close the WebDriver
    driver.quit()
