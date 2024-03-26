from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.cowin.gov.in/")


# Function to open FAQ and Partners links in new windows
def open_links_in_new_windows():
    faq_link = driver.find_element_by_link_text("FAQ")
    partners_link = driver.find_element_by_link_text("Partners")

    # Open FAQ link in a new window
    driver.execute_script("window.open(arguments[0], '_blank');", faq_link.get_attribute("href"))
    # Open Partners link in a new window
    driver.execute_script("window.open(arguments[0], '_blank');", partners_link.get_attribute("href"))


# Function to fetch window/frame IDs and display them
def display_window_ids():
    window_handles = driver.window_handles
    for handle in window_handles:
        print("Window ID:", handle)


# Function to close the new windows and switch back to the main window
def close_new_windows():
    window_handles = driver.window_handles
    # Close the new windows
    for handle in window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()
    # Switch back to the main window
    driver.switch_to.window(window_handles[0])


# Call functions to perform actions
open_links_in_new_windows()
time.sleep(3)  # Wait for new windows to open
print("Window IDs:")
display_window_ids()
close_new_windows()

# Close the main window
driver.quit()