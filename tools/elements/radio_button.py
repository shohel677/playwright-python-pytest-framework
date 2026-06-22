from tools.elements.base_components import BaseComponent


class CheckButton(BaseComponent):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    async def button_check(self):
        self.logger.info(f"Checking : {self.name}")
        await self.element.check()
        self.logger.info(f"Checking : {self.name}")

    async def is_button_check(self):
        self.logger.info(f"Is check: {self.name}")
        is_btn_check = await self.element.is_checked()
        assert is_btn_check
        self.logger.info(f"Is checked : {self.name} : {is_btn_check}")
