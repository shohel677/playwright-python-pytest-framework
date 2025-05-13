import pytest

from pages.automation_page import AutomationPage


@pytest.mark.details
def test_to_check_radio_button(without_login):
    home_page = AutomationPage(without_login)
    home_page.check_radio_button()


@pytest.mark.details
def test_to_alert_handling(without_login):
    automation = AutomationPage(without_login)
    automation.handle_alert()


@pytest.mark.details
def test_to_confirm_handling_accept(without_login):
    automation = AutomationPage(without_login)
    automation.handle_confirm(accept=True)


@pytest.mark.details
def test_to_confirm_handling_dismiss(without_login):
    automation = AutomationPage(without_login)
    automation.handle_confirm(accept=False)


@pytest.mark.details
def test_to_mouse_hover_reload(without_login):
    automation = AutomationPage(without_login)
    automation.mouse_hover_and_click_reload()


@pytest.mark.details
def test_to_verify_logo_in_iframe(without_login):
    automation = AutomationPage(without_login)
    automation.verify_logo_in_iframe()


@pytest.mark.details
def test_to_select_dropdown_option(without_login):
    automation = AutomationPage(without_login)
    automation.select_dropdown_option()


@pytest.mark.details
def test_to_handle_new_window_and_validate_logo(without_login):
    automation = AutomationPage(without_login)
    automation.handle_new_window_and_validate_logo()


@pytest.mark.details
def test_to_handle_new_tab_and_validate_logo(without_login):
    automation = AutomationPage(without_login)
    automation.handle_new_tab_and_validate_logo()
