from pages.base_page import BasePage
from pages.cart_page import CartPage
from tools.elements.button import Button
from tools.elements.label import Label


class SingleProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_page = CartPage(page)
        self.single_prod = Label(page.get_by_text("Sauce Labs Backpack"), "Sauce labs backpack")
        self.price = Label(page.locator(".inventory_details_price"), "Price of Sauce labs backpack")
        self.add_to_cart_button = Button(page.locator("#add-to-cart"), "Add to cart")
        self.remove_button = Button(page.get_by_role("button", name="Remove"), "Remove button")
        self.added_to_cart = Button(page.get_by_text("1"), "Added to cart")

    async def is_single_product_open(self):
        await self.single_prod.is_visible_assertion()
        await self.price.is_visible_assertion()
        await self.add_to_cart_button.is_visible_assertion()
        return self

    async def add_product_to_cart(self):
        await self.add_to_cart_button.single_click()
        await self.remove_button.expect_to_have_text("Remove")
        await self.added_to_cart.is_visible_assertion()
        return self

    async def goto_cart_page(self):
        await self.added_to_cart.single_click()
        return self.cart_page
