from tools.elements.base_components import BaseComponent


class Fill(BaseComponent):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def clear_fill(self, value):
        self.logger.info(f"Filling '{value}' in {self.name}")
        self.element.clear()
        self.element.fill(value)
        self.logger.info(f"Filled '{value}' in {self.name}")
