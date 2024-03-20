from selenium import webdriver


# Setting up Chrome WebDriver
driver = webdriver.Firefox()

# Navigating to the URL
url = "https://www.saucedemo.com/"
driver.get(url)

# Entering credentials and logging in
username = "Standard_user"
password = "secret_sauce"
username_input = driver.find_elements_by_id("user-name")
password_input = driver.find_elements_by_id("password")
login_button = driver.find_elements_by_id("login-button")

username_input.send_keys(username)
password_input.send_keys(password)
login_button.click()

# Fetching the required data
title = driver.title
current_url = driver.current_url
page_source = driver.page_source

# Printing the fetched data
print("Title:", title)
print("Current URL:", current_url)
print("Page Source:", page_source)

# Closing the WebDriver
driver.quit()