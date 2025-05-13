from pages.base_page import BasePage
from playwright.sync_api import Dialog, expect


class AutomationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.radioButton = page.locator(
            "//legend[text()='Radio Button Example']/following::label[contains(normalize-space(), 'Radio2')]/input"
        )
        self.suggestiveInput = page.locator("//legend[text()='Suggession Class Example']/following-sibling::input")
        self.option = page.locator("//div[text()='Bangladesh']")
        self.alertInput = page.locator(
            "//legend[text()='Switch To Alert Example']/following-sibling::input[@id='name']")
        self.alertBtn = page.locator("//input[@id='alertbtn']")
        self.confirmBtn = page.locator("//input[@id='confirmbtn']")
        self.mouseHoverBtn = page.locator("//button[text()='Mouse Hover']")
        self.reloadLink = page.locator("//div[@class='mouse-hover-content']/a[text()='Reload']")
        self.iframe = page.frame_locator("iframe#courses-iframe")  # Locator for the iframe element
        self.dropdown = page.locator("#dropdown-class-example")
        self.open_window_btn = page.locator("//button[@id='openwindow']")
        self.open_tab_btn = page.locator("//legend[text()='Switch Tab Example']/following-sibling::a")

    def check_radio_button(self):
        self.radioButton.check()
        assert self.radioButton.is_checked()

    def suggestive_dropdown(self):
        self.suggestiveInput.type("Bangladesh")
        input_val = self.suggestiveInput.input_value()
        assert input_val == "Bangladesh", f"Expected 'Bangladesh', but got '{input_val}'"

    def handle_alert(self):
        self.alertInput.fill("Shohel")

        def on_alert(dialog: Dialog):
            assert dialog.type == "alert"
            assert "Hello" in dialog.message
            dialog.accept()

        self.page.once("dialog", on_alert)
        self.alertBtn.click()

    def handle_confirm(self, accept: bool = True):
        self.alertInput.fill("Shohel")

        def on_confirm(dialog: Dialog):
            assert dialog.type == "confirm"
            assert "Are you sure" in dialog.message
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog", on_confirm)
        self.confirmBtn.click()

    def mouse_hover_and_click_reload(self):
        self.mouseHoverBtn.hover()
        expect(self.reloadLink).to_be_visible()
        self.reloadLink.click()

    def verify_logo_in_iframe(self):
        logo = self.iframe.locator("//div[@class='logo']")
        expect(logo).to_be_visible()

    def select_dropdown_option(self):
        self.dropdown.select_option(value="option2")
        # Verify if the correct option is selected
        selected_option = self.dropdown.locator("option:checked")
        expect(selected_option).to_have_text("Option2")

    def handle_new_window_and_validate_logo(self):
        # Listen for new page (window/tab)
        with self.page.context.expect_page() as new_page_info:
            self.open_window_btn.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        logo = new_page.locator("(//div[@class='logo']/a/img[@alt='Logo'])[1]")
        expect(logo).to_be_visible()
        print("Logo is visible in the new window.")
        new_page.close()
        expect(self.open_window_btn).to_be_visible()

    def handle_new_tab_and_validate_logo(self):
        # Listen for new page (window/tab)
        with self.page.context.expect_page() as new_page_info:
            self.open_tab_btn.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        logo = new_page.locator("(//div[@class='logo']/a/img[@alt='Logo'])[1]")
        expect(logo).to_be_visible()
        print("✅ Logo is visible in the new window.")
        new_page.close()
        expect(self.open_window_btn).to_be_visible()
