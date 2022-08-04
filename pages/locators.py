from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#text')
    SUGGEST_FIELD = (By.CSS_SELECTOR, '.mini-suggest__popup_visible')
    LOOKUP_TABLE = (By.CSS_SELECTOR, '#search-result')
    TENZOR_LINK = (By.CSS_SELECTOR, '#search-result li a')


class ImagesPageLocators:
    IMAGES_LINK = (By.CSS_SELECTOR, '[data-id=images]')
    FIRST_CATEGORY_OF_IMAGES = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    NAME_FIRST_CATEGORY_IN_SEARCH_FIELD = (By.CSS_SELECTOR, '.mini-suggest__input')
    FIRST_IMAGE = (By.CSS_SELECTOR, '.justifier__item_first')
    OPENED_IMAGE = (By.CSS_SELECTOR, '.MMImageContainer [src]')
    BTN_NEXT = (By.CSS_SELECTOR, '.MediaViewer_theme_fiji-ButtonNext .CircleButton-Icon')
    BTN_PREV = (By.CSS_SELECTOR, '.MediaViewer_theme_fiji-ButtonPrev .CircleButton-Icon')
