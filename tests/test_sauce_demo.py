import pytest

from pages.home_page import HomePage


@pytest.mark.regression
def test_to_check_homepage(logged_in_page):
    home_page = HomePage(logged_in_page)
    home_page.get_title().get_curr_url()


@pytest.mark.regression
def test_to_open_a_product(logged_in_page):
    home_page = HomePage(logged_in_page)
    home_page.get_title().get_curr_url().open_a_product().is_single_product_open()


@pytest.mark.regression
@pytest.mark.smoke
def test_to_add_product_to_cart(logged_in_page):
    home_page = HomePage(logged_in_page)
    product_page = home_page.get_title().get_curr_url().open_a_product().is_single_product_open()
    product_page.add_product_to_cart()


@pytest.mark.regression
@pytest.mark.smoke
def test_to_open_cart_page(logged_in_page):
    home_page = HomePage(logged_in_page)
    product_page = home_page.get_title().get_curr_url().open_a_product().is_single_product_open()
    cart_page = product_page.add_product_to_cart().goto_cart_page()
    cart_page.product_visibility()
