from pages.base_page import BasePage
from pages.single_product_page import SingleProductPage
from tools.elements.label import Label


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.single_product_page = SingleProductPage(page)
        self.product = Label(page.get_by_text("Sauce Labs Backpack"), "Product header")

    async def get_title(self):
        title = await self.page.title()
        assert "Swag Labs" in title
        return self

    async def get_curr_url(self):
        current_url = self.page.url
        assert "https://www.saucedemo.com/inventory.html" in current_url
        return self

    async def open_a_product(self):
        await self.product.single_click()
        return self.single_product_page
