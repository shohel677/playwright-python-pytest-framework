import asyncio
import base64
import os
import shutil
from datetime import datetime

import pytest
from playwright.async_api import async_playwright
from pytest_html import extras

from pages.login_page import LoginPage

REPORT_DIR = "reports"


@pytest.fixture
async def browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        yield browser
        await browser.close()


@pytest.fixture
async def context(browser):
    context = await browser.new_context(viewport={"width": 1500, "height": 1080})
    yield context
    await asyncio.sleep(3)
    await context.close()


@pytest.fixture
async def page(context, request):
    page = await context.new_page()
    yield page

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = request.node.name
    file_name = f"{test_name}_passed_{timestamp}.png"
    file_path = os.path.join("reports", file_name)

    await page.screenshot(path=file_path, full_page=True)
    full_path = os.path.abspath(file_path)

    with open(file_path, "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode("utf-8")

    call_report = getattr(request.node, "rep_call", None)
    if call_report and call_report.passed:
        print(f"\nScreenshot saved: {full_path}")
        call_report.extras = getattr(call_report, "extras", [])
        call_report.extras.append(extras.image(encoded_img, mime_type="image/png"))

    await page.close()


@pytest.fixture
async def logged_in_page(page, request):
    url = request.config.getoption("url")
    login_page = LoginPage(page)
    await login_page.goto(url)
    await login_page.login("standard_user", "secret_sauce")
    return page


@pytest.fixture
async def without_login(page, request):
    url = request.config.getoption("url")
    login_page = LoginPage(page)
    await login_page.goto(url)
    return page


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url", action="store", default="https://www.saucedemo.com/", help="Environment url"
    )
    parser.addoption(
        "--username", action="store", default="standard_user", help="Environment url"
    )
    parser.addoption(
        "--password", action="store", default="secret_sauce", help="Environment url"
    )


def pytest_sessionstart(session):
    reports_path = os.path.join(os.getcwd(), "reports")
    if os.path.exists(reports_path):
        shutil.rmtree(reports_path)
    os.makedirs(reports_path)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
