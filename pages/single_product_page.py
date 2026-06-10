from pages.base_page import BasePage
from pages.cart_page import CartPage
from playwright.sync_api import expect


class SingleProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_page = CartPage(page)
        self.single_prod = page.get_by_text("Sauce Labs Backpack")
        self.price = page.locator(".inventory_details_price")
        self.add_to_cart_button = page.locator("#add-to-cart")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.added_to_cart = page.get_by_text("1")

    def is_single_product_open(self):
        assert self.single_prod.is_visible()
        assert self.price.is_visible()
        assert self.add_to_cart_button.is_visible()
        return self

    def add_product_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.remove_button).to_have_text("Remove")
        assert self.added_to_cart.is_visible()
        return self

    def goto_cart_page(self):
        self.added_to_cart.click()
        return self.cart_page

