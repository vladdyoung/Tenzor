import allure
import pytest
from pages.search_page import SearchPage


@allure.feature('Test Yandex')
@allure.story('Search in Yandex')
@allure.step('Checking that search field is present on the page')
@pytest.mark.search_field_is_present
def test_search_field_is_present(browser, base_url):
    search_page = SearchPage(browser, base_url)
    search_page.open()
    search_page.should_be_search_field()


@allure.feature('Test Yandex')
@allure.story('Search in Yandex')
@allure.step('Checking that suggest field has appeared')
@pytest.mark.suggest_field_is_appear
def test_suggest_field_is_appear(browser, base_url):
    search_page = SearchPage(browser, base_url)
    search_page.enter_company_name_in_search_field()
    search_page.should_be_suggest_field_is_appear()


@allure.feature('Test Yandex')
@allure.story('Search in Yandex')
@allure.step('Checking that the lookup table is present')
@pytest.mark.lookup_table_is_present
def test_lookup_table_is_present(browser, base_url):
    search_page = SearchPage(browser, base_url)
    search_page.click_enter_btn()
    search_page.should_be_lookup_table()


@allure.feature('Test Yandex')
@allure.story('Search in Yandex')
@allure.step('Checking redirect on tenzor.ru')
@pytest.mark.redirect_on_tenzor
def test_redirect_on_tenzor(browser, base_url):
    search_page = SearchPage(browser, base_url)
    search_page.click_tenzor_link()
    search_page.should_be_redirect_on_tenzor_ru()
