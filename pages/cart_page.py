from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_details = page.get_by_text("Sauce Labs Backpack")

    def product_visibility(self):
        self.product_details.is_visible()
        return self
