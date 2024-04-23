from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the IMDb search page
url = "https://www.imdb.com/search/name/"

# Initialize Chrome webdriver
driver = webdriver.Chrome()
driver.get(url)

# Function to select a value from a dropdown
def select_dropdown_value(dropdown, value):
    dropdown.click()
    driver.find_element(By.XPATH, f"//option[text()='{value}']").click()

# Explicit wait until the year dropdown is clickable
year_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='birth_year']"))
)

# Select the year from the dropdown
select_dropdown_value(year_dropdown, "1990")

# Explicit wait until the month dropdown is clickable
month_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='birth_month']"))
)

# Select the month from the dropdown
select_dropdown_value(month_dropdown, "March")

# Explicit wait until the day dropdown is clickable
day_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='birth_day']"))
)

# Select the day from the dropdown
select_dropdown_value(day_dropdown, "15")

# Find and click the search button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']"))
)
search_button.click()

# Close the webdriver
driver.quit()


