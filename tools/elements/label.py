from tools.elements.base_components import BaseComponent


class Label(BaseComponent):
    def __init__(self, locator, name):
        super().__init__(locator, name)
