from pages.base_page import BasePage
from pages.locators import SearchPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):
    def should_be_search_field(self):
        self.logger.info(f'Find element ({SearchPageLocators.SEARCH_FIELD[1]}) '
                         f'by using ({SearchPageLocators.SEARCH_FIELD[0]})')
        assert self.is_element_present(*SearchPageLocators.SEARCH_FIELD), \
            ('Search field is not found', self.logger.error('Search field is not found'))[0]
        self.logger.info('Search field is present on the page')

    def enter_company_name_in_search_field(self):
        search_field = self.browser.find_element(*SearchPageLocators.SEARCH_FIELD)
        search_field.clear()
        self.logger.info('Enter "Тензор" in search field')
        search_field.send_keys('Тензор')

    def should_be_suggest_field_is_appear(self):
        try:
            self.logger.info('Find suggest field)')
            WebDriverWait(self.browser, 3, TimeoutException).until(EC.visibility_of_element_located
                                                                   (SearchPageLocators.SUGGEST_FIELD))
            self.logger.info('Suggest field is appeared')
        except:
            self.logger.error('Suggest field has not appeared')
            raise AssertionError('Suggest field has not appeared')

    def click_enter_btn(self):
        self.logger.info('Click ENTER')
        self.browser.find_element(*SearchPageLocators.SEARCH_FIELD).send_keys(Keys.ENTER)

    def should_be_lookup_table(self):
        self.logger.info(f'Find element ({SearchPageLocators.LOOKUP_TABLE[1]}) '
                         f'by using ({SearchPageLocators.LOOKUP_TABLE[0]})')
        assert self.is_element_present(*SearchPageLocators.LOOKUP_TABLE), \
            ('Lookup table is not found', self.logger.error('Lookup table is not found'))[0]
        self.logger.info('Lookup table is present')

    def click_tenzor_link(self):
        self.logger.info('Tenzor link is present')
        self.browser.find_element(*SearchPageLocators.TENZOR_LINK).click()

    def should_be_redirect_on_tenzor_ru(self):
        self.logger.info('Checking redirect on tenzor.ru')
        self.browser.switch_to_window(self.browser.window_handles[1])
        assert self.browser.current_url == 'https://tensor.ru/', \
            ('Page wrong. Redirect is fail!', self.logger.error('Page wrong. Redirect is fail!'))[0]
        self.logger.info('Successful redirect on tenzor.ru')
