import logging

from playwright.async_api import expect


class BaseComponent:

    def __init__(self, element, name):
        self.element = element
        self.name = name
        self.logger = logging.getLogger(self.__class__.__name__)

    async def single_click(self):
        self.logger.info(f"Clicking {self.name}")
        await self.element.click()
        self.logger.info(f"Clicked {self.name}")

    async def is_visible_assertion(self):
        self.logger.info(f"Checking visibility of: {self.name}")
        is_displayed = await self.element.is_visible()
        self.logger.info(f"{self.name}  is visible:  {is_displayed}")
        assert is_displayed
        return is_displayed

    def get_wrapped_element(self):
        self.logger.info(f"Wrapped element: {self.name}")
        return self.element

    async def expect_to_have_text(self, text):
        self.logger.info(f"Expecting text {text} for : {self.name}")
        have_text = await expect(self.element).to_have_text(text)
        self.logger.info(f"Expected text {text} for : {self.name} is present: {have_text}")
        return have_text

    async def expect_to_be_visible(self):
        self.logger.info(f"Expecting element to be visible : {self.name}")
        is_visible = await expect(self.element).to_be_visible()
        self.logger.info(f"Expected element visible : {is_visible} ")
        return is_visible

    async def mouse_hover(self):
        self.logger.info(f"Hovering : {self.name}")
        await self.element.hover()
