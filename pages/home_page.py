from pages.base_page import BasePage
from pages.single_product_page import SingleProductPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.single_product_page = SingleProductPage(page)
        self.product = page.locator("//div[text()='Sauce Labs Backpack']/parent::a")

    def get_title(self):
        title = self.page.title()
        assert "Swag Labs" in title
        return self

    def get_curr_url(self):
        current_url = self.page.url
        assert "https://www.saucedemo.com/inventory.html" in current_url
        return self

    def open_a_product(self):
        self.product.click()
        return self.single_product_page
