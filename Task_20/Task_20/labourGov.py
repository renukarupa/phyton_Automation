import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to download file
def download_file(driver, url, download_path, file_name):
    driver.get(url)
    file_path = os.path.join(download_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    driver.find_element(By.LINK_TEXT, "Click here to download file").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "download")))

# Set up Chrome WebDriver (make sure to have chromedriver installed and in PATH)
driver = webdriver.Chrome()

# Set download directory
download_dir = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Task 1: Go to the "documents" menu and download the monthly progress report
driver.get("https://labour.gov.in/")
documents_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Documents")))
documents_menu.click()
download_file(driver, driver.current_url, download_dir, "monthly_progress_report.pdf")

# Task 2: Go to the "Media" menu and click on the "Photo Gallery" sub-menu
driver.get("https://labour.gov.in/")
media_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Media")))
ActionChains(driver).move_to_element(media_menu).perform()
photo_gallery_submenu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Photo Gallery")))
photo_gallery_submenu.click()

# Close the browser
driver.quit()
