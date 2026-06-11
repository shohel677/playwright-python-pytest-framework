import logging
from playwright.sync_api import expect


class BaseComponent:

    def __init__(self, element, name):
        self.element = element
        self.name = name
        # Initialize logger for this page
        self.logger = logging.getLogger(self.__class__.__name__)

    def single_click(self):
        self.logger.info(f"Clicking {self.name}")
        self.element.click()
        self.logger.info(f"Clicked {self.name}")

    def is_visible_assertion(self):
        self.logger.info(f"Checking visibility of: {self.name}")
        is_displayed = self.element.is_visible()
        assert is_displayed
        self.logger.info(f"{self.name}  is visible:  {is_displayed}")

    def get_wrapped_element(self):
        self.logger.info(f"Wrapped element: {self.name}")
        return self.element

    def expect_to_have_text(self, text):
        self.logger.info(f"Expecting text {text} for : {self.name}")
        expect(self.element).to_have_text(text)
        self.logger.info(f"Expected text {text} for : {self.name} is present")
