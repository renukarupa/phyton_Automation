from selenium.webdriver.common.by import By

class IMDbSearchPageLocators:
    YEAR_DROPDOWN = (By.NAME, 'birth_year')
    MONTH_DROPDOWN = (By.NAME, 'birth_month')
    DAY_DROPDOWN = (By.NAME, 'birth_day')
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")