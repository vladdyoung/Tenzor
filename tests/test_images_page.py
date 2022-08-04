import allure
import pytest
from pages.images_page import ImagesPage


@allure.feature('Test Yandex')
@allure.story('Images in Yandex')
@allure.step('Checking images link is present on page')
@pytest.mark.images_link_is_present
def test_images_link_is_present(browser, base_url):
    images_page = ImagesPage(browser, base_url)
    images_page.open()
    images_page.should_be_images_link()


@allure.feature('Test Yandex')
@allure.story('Images in Yandex')
@allure.step('Checking redirect on images page')
@pytest.mark.redirect_on_images_page
def test_redirect_on_images_page(browser, base_url):
    images_page = ImagesPage(browser, base_url)
    images_page.click_on_images_link()
    images_page.should_be_redirect_on_images_page()


@allure.feature('Test Yandex')
@allure.story('Images in Yandex')
@allure.step('Checking that name first category images in search field is displayed')
@pytest.mark.first_category_images_in_search_field
def test_first_category_images_in_search_field(browser, base_url):
    images_page = ImagesPage(browser, base_url)
    images_page.open_first_category_of_images()
    images_page.should_be_name_first_category_images_in_search_field()


@allure.feature('Test Yandex')
@allure.story('Images in Yandex')
@allure.step('Checking that first images opened after click')
@pytest.mark.first_category_images_opened_after_click
def test_first_category_images_opened_after_click(browser, base_url):
    images_page = ImagesPage(browser, base_url)
    images_page.open_first_image()
    images_page.should_be_opened_first_image()


@allure.feature('Test Yandex')
@allure.story('Images in Yandex')
@allure.step('Checking that image has changed')
@pytest.mark.image_changed
def test_image_changed(browser, base_url):
    images_page = ImagesPage(browser, base_url)
    images_page.click_on_next_image_btn()
    images_page.should_be_next_image()


@allure.feature('Test Yandex')
@allure.story('Images in Yandex')
@allure.step('Checking that image returned')
@pytest.mark.image_returned
def test_image_returned(browser, base_url):
    images_page = ImagesPage(browser, base_url)
    images_page.click_on_prev_image_btn()
    images_page.should_be_returned_image()
