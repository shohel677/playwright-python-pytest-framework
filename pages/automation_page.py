from pages.base_page import BasePage
from playwright.async_api import Dialog, expect


class AutomationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.radioButton = page.locator("input[value='radio2']")
        self.suggestiveInput = page.get_by_placeholder("Type to Select Countries")
        self.option = page.get_by_text("Bangladesh")
        self.alertInput = page.locator("#name")
        self.alertBtn = page.locator("#alertbtn")
        self.confirmBtn = page.locator("#confirmbtn")
        self.mouseHoverBtn = page.get_by_role("button", name="Mouse Hover")
        self.reloadLink = page.get_by_text("Reload")
        self.iframe = page.frame_locator("iframe#courses-iframe")
        self.dropdown = page.locator("#dropdown-class-example")
        self.open_window_btn = page.locator("#openwindow")
        self.open_tab_btn = page.locator("#opentab")

    async def check_radio_button(self):
        await self.radioButton.check()
        assert await self.radioButton.is_checked()

    async def suggestive_dropdown(self):
        await self.suggestiveInput.type("Bangladesh")
        input_val = await self.suggestiveInput.input_value()
        assert input_val == "Bangladesh", f"Expected 'Bangladesh', but got '{input_val}'"

    async def handle_alert(self):
        await self.alertInput.fill("Shohel")

        async def on_alert(dialog: Dialog):
            assert dialog.type == "alert"
            assert "Hello" in dialog.message
            await dialog.accept()

        self.page.once("dialog", on_alert)
        await self.alertBtn.click()

    async def handle_confirm(self, accept: bool = True):
        await self.alertInput.fill("Shohel")

        async def on_confirm(dialog: Dialog):
            assert dialog.type == "confirm"
            assert "Are you sure" in dialog.message
            if accept:
                await dialog.accept()
            else:
                await dialog.dismiss()

        self.page.once("dialog", on_confirm)
        await self.confirmBtn.click()

    async def mouse_hover_and_click_reload(self):
        await self.mouseHoverBtn.hover()
        await expect(self.reloadLink).to_be_visible()
        await self.reloadLink.click()

    async def verify_logo_in_iframe(self):
        logo = self.iframe.locator("div.pull-left.logo-outer img[src='assets/images/rs_logo.png']")
        await expect(logo).to_be_visible()

    async def select_dropdown_option(self):
        await self.dropdown.select_option(value="option2")
        selected_option = self.dropdown.locator("option:checked")
        await expect(selected_option).to_have_text("Option2")

    async def handle_new_window_and_validate_logo(self):
        async with self.page.context.expect_page() as new_page_info:
            await self.open_window_btn.click()

        new_page = await new_page_info.value
        await new_page.wait_for_load_state()

        logo = new_page.locator("img[alt='Logo']")
        await expect(logo).to_be_visible()
        print("Logo is visible in the new window.")
        await new_page.close()
        await expect(self.open_window_btn).to_be_visible()

    async def handle_new_tab_and_validate_logo(self):
        async with self.page.context.expect_page() as new_page_info:
            await self.open_tab_btn.click()

        new_page = await new_page_info.value
        await new_page.wait_for_load_state()

        logo = new_page.locator("img[alt='Logo']")
        await expect(logo).to_be_visible()
        print("Logo is visible in the new tab.")
        await new_page.close()
        await expect(self.open_window_btn).to_be_visible()
