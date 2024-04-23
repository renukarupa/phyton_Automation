from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# URL of the page with draggable elements
url = "https://jqueryui.com/droppable/"

# Initialize Chrome webdriver
driver = webdriver.Chrome()
driver.get(url)

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '.demo-frame'))

# Find the draggable element
draggable = driver.find_element(By.ID, "draggable")

# Find the droppable element
droppable = driver.find_element(By.ID, "droppable")

# Perform the drag and drop operation
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Switch back to the default content
driver.switch_to.default_content()

# Close the webdriver
driver.quit()