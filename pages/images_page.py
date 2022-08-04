from pages.base_page import BasePage
from pages.locators import ImagesPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImagesPage(BasePage):
    def should_be_images_link(self):
        self.logger.info(f'Find element ({ImagesPageLocators.IMAGES_LINK[1]}) '
                         f'by using ({ImagesPageLocators.IMAGES_LINK[0]})')
        assert self.is_element_present(*ImagesPageLocators.IMAGES_LINK), \
            ('Images link is not found', self.logger.error('Images link is not found'))[0]
        self.logger.info('Images link is present on page')

    def click_on_images_link(self):
        self.logger.info('Click on images link')
        self.browser.find_element(*ImagesPageLocators.IMAGES_LINK).click()

    def should_be_redirect_on_images_page(self):
        self.logger.info('Checking redirect on "https://yandex.ru/images/"')
        self.browser.switch_to_window(self.browser.window_handles[1])
        assert 'https://yandex.ru/images/' in self.browser.current_url, \
            ('Page wrong. Redirect is fail!', self.logger.error('Page wrong. Redirect is fail!'))[0]
        self.logger.info('Successful redirect on images page')

    def open_first_category_of_images(self):
        self.logger.info(f'Find element ({ImagesPageLocators.FIRST_CATEGORY_OF_IMAGES[1]}) '
                         f'by using ({ImagesPageLocators.FIRST_CATEGORY_OF_IMAGES[0]})')
        self.first_category_of_images = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY_OF_IMAGES).text
        self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY_OF_IMAGES).click()
        self.name_first_category_in_search_field = self.browser.find_element \
            (*ImagesPageLocators.NAME_FIRST_CATEGORY_IN_SEARCH_FIELD).get_attribute('value')
        self.logger.info('Successful open')

    def should_be_name_first_category_images_in_search_field(self):
        self.logger.info('Names matching check')
        assert self.first_category_of_images == self.name_first_category_in_search_field, \
            ('Names do not match', self.logger.error('Names do not match'))[0]
        self.logger.info('Names matching')
        try:
            self.logger.info('Checking display name first category images in search field')
            WebDriverWait(self.browser, 3, TimeoutException). \
                until(EC.text_to_be_present_in_element_value
                      (ImagesPageLocators.NAME_FIRST_CATEGORY_IN_SEARCH_FIELD,
                       self.name_first_category_in_search_field)), \
            self.logger.info('Name first category images in search field is displayed')
        except:
            self.logger.error('Name not displayed')
            raise AssertionError('Name not displayed')

    def open_first_image(self):
        self.logger.info('Open first image')
        self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE).click()
        self.logger.info('Successful open')

    def should_be_opened_first_image(self):
        self.logger.info(f'Find element ({ImagesPageLocators.FIRST_IMAGE[1]}) '
                         f'by using ({ImagesPageLocators.FIRST_IMAGE[0]})')
        assert self.is_element_present(*ImagesPageLocators.FIRST_IMAGE), \
            ('Image not opened', self.logger.error('Image not opened'))[0]
        self.logger.info('First images open successful')

    def click_on_next_image_btn(self):
        self.logger.info('Click on next image btn')
        self.browser.opened_first_image = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute(
            'src')
        self.browser.find_element(*ImagesPageLocators.BTN_NEXT).click()

    def should_be_next_image(self):
        self.logger.info('Checking that image has changed')
        self.browser.opened_second_image = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute(
            'src')
        assert self.browser.opened_first_image != self.browser.opened_second_image, \
            ('Image not changed', self.logger.error('Image not changed'))[0]
        self.logger.info('Successful changed')

    def click_on_prev_image_btn(self):
        self.logger.info('Click on prev image btn')
        self.browser.find_element(*ImagesPageLocators.BTN_PREV).click()

    def should_be_returned_image(self):
        self.logger.info('Checking that image returned')
        self.browser.opened_returned_image = self.browser.find_element(*ImagesPageLocators.OPENED_IMAGE).get_attribute(
            'src')
        assert self.browser.opened_first_image == self.browser.opened_returned_image, \
            ('Image not returned', self.logger.error('Image not returned'))[0]
        self.logger.info('Successful image returned')
