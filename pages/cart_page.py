import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    value_product = "//div[@class='product__item-title mb20']"
    make_order_button = "//a[@class='btn btn-orange mb10']"


    """Getters"""

    def get_value_product(self):
        return (WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_product))))

    def get_make_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.make_order_button)))


    """Actions"""

    def click_make_order_button(self):
        self.get_make_order_button().click()
        print("Get Make Order Button")


    """Methods"""

    def product_confirmation(self):
        self.assert_word(self.get_value_product(), "Мешок Tramp спальный Mersey R оранжево-серый TRS-019")
        self.get_screenshot()
        self.click_make_order_button()








