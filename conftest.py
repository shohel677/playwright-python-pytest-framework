import base64
import shutil
from datetime import datetime

import pytest
import pytest_html
from playwright.sync_api import sync_playwright
from pytest_html import extras

from pages.login_page import LoginPage
import os


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(
        viewport={"width": 1500, "height": 1080}
    )
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return page


REPORT_DIR = "reports"


# Clear reports folder before run
def pytest_sessionstart(session):
    reports_path = os.path.join(os.getcwd(), "reports")
    if os.path.exists(reports_path):
        shutil.rmtree(reports_path)
    os.makedirs(reports_path)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.passed:
        page = item.funcargs.get("page", None)
        if page:
            # Generate filename
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = report.nodeid.split("::")[-1]
            file_name = f"{test_name}_passed_{timestamp}.png"
            file_path = os.path.join("reports", file_name)

            # Take screenshot
            page.screenshot(path=file_path, full_page=True)

            # Print path to console
            full_path = os.path.abspath(file_path)
            print(f"\n📸 Screenshot saved: {full_path}")

            # Embed in HTML report (if using self-contained)
            with open(file_path, "rb") as f:
                encoded_img = base64.b64encode(f.read()).decode("utf-8")
            report.extras = getattr(report, "extras", [])
            report.extras.append(extras.image(encoded_img, mime_type="image/png"))
