import pytest

from api.api_page import PageAPI


@pytest.fixture(scope="module")
def post_api():
    return PageAPI()


@pytest.mark.api
def test_get_post(post_api):
    response = post_api.get_post(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.api
def test_create_post(post_api):
    response = post_api.create_post()
    assert response.status_code == 201
    assert response.json()["title"] == "foo"


@pytest.mark.api
def test_update_post(post_api):
    response = post_api.update_post(1)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


@pytest.mark.api
def test_patch_post(post_api):
    response = post_api.patch_post(1)
    assert response.status_code == 200
    assert response.json()["title"] == "patched title"


@pytest.mark.api
def test_delete_post(post_api):
    response = post_api.delete_post(1)
    assert response.status_code == 200
