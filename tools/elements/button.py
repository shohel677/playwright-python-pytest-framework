from tools.elements.base_components import BaseComponent


class Button(BaseComponent):
    def __init__(self, locator, name):
        super().__init__(locator, name)
