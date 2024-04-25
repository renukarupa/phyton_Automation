from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import IMDbSearchPageLocators

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def select_dropdown_value(self, dropdown, value):
        option_xpath = f"//option[text()='{value}']"
        self.driver.find_element_by_xpath(option_xpath).click()

    def fill_date_and_search(self, year, month, day):
        year_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IMDbSearchPageLocators.YEAR_DROPDOWN))
        self.select_dropdown_value(year_dropdown, year)

        month_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IMDbSearchPageLocators.MONTH_DROPDOWN))
        self.select_dropdown_value(month_dropdown, month)

        day_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IMDbSearchPageLocators.DAY_DROPDOWN))
        self.select_dropdown_value(day_dropdown, day)

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IMDbSearchPageLocators.SEARCH_BUTTON))
        search_button.click()
