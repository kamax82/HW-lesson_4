import pytest

@pytest.fixture
def test_dog_url():
    return ('https://dog.ceo/dog-api/')


@pytest.fixture
def test_openbrewerydb_url():
    return ('https://www.openbrewerydb.org/')


@pytest.fixture
def test_jsonplaceholder_url():
    return ('https://jsonplaceholder.typicode.com/')


@pytest.fixture
def url_yandex_param(request):
    return request.config.getoption('--url', 'status_code')