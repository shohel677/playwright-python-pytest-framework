import logging


class BaseComponent:

    def __init__(self, element, name):
        self.element = element
        self.name = name
        # Initialize logger for this page
        self.logger = logging.getLogger(self.__class__.__name__)

    def single_click(self):
        self.logger.info("Clicking " + self.name)
        self.element.click()
        self.logger.info("Clicked " + self.name)

    def is_visible_assertion(self):
        self.logger.info(self.name + " is visible")
        assert self.element.is_visible()
