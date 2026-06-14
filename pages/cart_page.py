from pages.base_page import BasePage
from tools.elements.label import Label


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_details = Label(page.get_by_text("Sauce Labs Backpack"), "Product header")

    def product_visibility(self):
        self.product_details.is_visible_assertion()
        return self
