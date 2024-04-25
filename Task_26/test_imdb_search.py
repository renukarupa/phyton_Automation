import pytest
from selenium import webdriver
from imdb_search_page import IMDbSearchPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_imdb_search(browser):
    browser.get("https://www.imdb.com/search/name/")
    imdb_search_page = IMDbSearchPage(browser)
    imdb_search_page.fill_date_and_search("1990", "March", "15")
