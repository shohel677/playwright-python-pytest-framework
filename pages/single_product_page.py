from pages.base_page import BasePage
from pages.cart_page import CartPage


class SingleProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_page = CartPage(page)
        self.single_prod = page.locator("//div[@class='inventory_details_name large_size']")
        self.price = page.locator("//div[@class='inventory_details_price']")
        self.add_to_cart_button = page.locator("//button[@id='add-to-cart']")
        self.remove_button = page.locator("//button[@id='remove']")
        self.added_to_cart = page.locator("//span[text()='1']")

    def is_single_product_open(self):
        self.single_prod.is_visible()
        self.price.is_visible()
        self.add_to_cart_button.is_visible()
        return self

    def add_product_to_cart(self):
        self.add_to_cart_button.click()
        self.remove_button.is_visible()
        self.added_to_cart.is_visible()
        return self

    def goto_cart_page(self):
        self.added_to_cart.click()
        return self.cart_page

