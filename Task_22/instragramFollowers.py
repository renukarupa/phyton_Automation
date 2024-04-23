from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the Instagram profile
url = "https://www.instagram.com/guvioffical/"

# Initialize Chrome webdriver
driver = webdriver.Chrome()
driver.get(url)

# Wait for the follower count element to be visible
followers_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/guvioffical/followers/"]/span')))
followers_count = followers_element.get_attribute("title")

# Wait for the following count element to be visible
following_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/guvioffical/following/"]/span')))
following_count = following_element.get_attribute("title")

# Print the counts
print("Followers:", followers_count)
print("Following:", following_count)

# Close the webdriver
driver.quit()