from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_details = page.locator(
            "//div[text()='Sauce Labs Backpack']/parent::a/ancestor::div[@class='cart_item']/div[text("
            ")='1']/following-sibling::div/div[@class='item_pricebar']/div[contains(normalize-space(), '$29.99')]")

    def product_visibility(self):
        self.product_details.is_visible()
        return self
