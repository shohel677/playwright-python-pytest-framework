from pages.base_page import BasePage
from pages.cart_page import CartPage
from playwright.sync_api import expect
from components.button import Button
from components.fill import Fill


class SingleProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_page = CartPage(page)
        self.single_prod = page.get_by_text("Sauce Labs Backpack")
        self.price = page.locator(".inventory_details_price")
        self.add_to_cart_button = Button(page.locator("#add-to-cart"), "Add to cart")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.added_to_cart = Button(page.get_by_text("1"), "Added to cart")

    def is_single_product_open(self):
        assert self.single_prod.is_visible()
        assert self.price.is_visible()
        self.add_to_cart_button.is_visible_assertion()
        return self

    def add_product_to_cart(self):
        self.add_to_cart_button.single_click()
        expect(self.remove_button).to_have_text("Remove")
        self.added_to_cart.is_visible_assertion()
        return self

    def goto_cart_page(self):
        self.added_to_cart.single_click()
        return self.cart_page
