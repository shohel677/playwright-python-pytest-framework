import pytest

from pages.automation_page import AutomationPage


@pytest.mark.details
async def test_to_check_radio_button(without_login):
    automation = AutomationPage(without_login)
    await automation.check_radio_button()


@pytest.mark.details
async def test_to_alert_handling(without_login):
    automation = AutomationPage(without_login)
    await automation.handle_alert()


@pytest.mark.details
async def test_to_confirm_handling_accept(without_login):
    automation = AutomationPage(without_login)
    await automation.handle_confirm(accept=True)


@pytest.mark.details
async def test_to_confirm_handling_dismiss(without_login):
    automation = AutomationPage(without_login)
    await automation.handle_confirm(accept=False)


@pytest.mark.details
async def test_to_mouse_hover_reload(without_login):
    automation = AutomationPage(without_login)
    await automation.mouse_hover_and_click_reload()


@pytest.mark.details
async def test_to_verify_logo_in_iframe(without_login):
    automation = AutomationPage(without_login)
    await automation.verify_logo_in_iframe()


@pytest.mark.details
async def test_to_select_dropdown_option(without_login):
    automation = AutomationPage(without_login)
    await automation.select_dropdown_option()


@pytest.mark.details
async def test_to_handle_new_window_and_validate_logo(without_login):
    automation = AutomationPage(without_login)
    await automation.handle_new_window_and_validate_logo()


@pytest.mark.details
async def test_to_handle_new_tab_and_validate_logo(without_login):
    automation = AutomationPage(without_login)
    await automation.handle_new_tab_and_validate_logo()
