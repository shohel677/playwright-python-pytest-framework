from components.base_components import BaseComponent


class Fill(BaseComponent):
    def __init__(self, locator, name):
        super().__init__(locator, name)
        
    def clear_fill(self, value):
        self.logger.info("Filling " + value + " in " + self.name)
        self.element.clear()
        self.element.fill(value)
        self.logger.info("Filled " + value + " in " + self.name)
