import pytest

from pages.home_page import HomePage


@pytest.mark.regression
async def test_to_check_homepage(logged_in_page):
    home_page = HomePage(logged_in_page)
    await home_page.get_title()
    await home_page.get_curr_url()


@pytest.mark.regression
async def test_to_open_a_product(logged_in_page):
    home_page = HomePage(logged_in_page)
    await home_page.get_title()
    await home_page.get_curr_url()
    product_page = await home_page.open_a_product()
    await product_page.is_single_product_open()


@pytest.mark.regression
@pytest.mark.smoke
async def test_to_add_product_to_cart(logged_in_page):
    home_page = HomePage(logged_in_page)
    await home_page.get_title()
    await home_page.get_curr_url()
    product_page = await home_page.open_a_product()
    await product_page.is_single_product_open()
    await product_page.add_product_to_cart()


@pytest.mark.regression
@pytest.mark.smoke
async def test_to_open_cart_page(logged_in_page):
    home_page = HomePage(logged_in_page)
    await home_page.get_title()
    await home_page.get_curr_url()
    product_page = await home_page.open_a_product()
    await product_page.is_single_product_open()
    product_page = await product_page.add_product_to_cart()
    cart_page = await product_page.goto_cart_page()
    await cart_page.product_visibility()
