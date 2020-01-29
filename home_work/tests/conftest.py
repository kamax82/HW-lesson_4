import pytest

@pytest.fixture
def test_dog_url():
    return ('https://dog.ceo/dog-api/')


@pytest.fixture
def test_openbrewerydb_url():
    return ('https://api.openbrewerydb.org/breweries')


@pytest.fixture
def test_jsonplaceholder_url():
    return ('https://jsonplaceholder.typicode.com/posts/')


@pytest.fixture
def url_yandex_param(request):
    return request.config.getoption('--url', 'status_code')

def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='Url to make request to. Default ya.ru')
    parser.addoption('--status_code', default=200, help='Status code response which expected. Default 200')

@pytest.fixture
def request_params(request):
    config_param = {}
    config_param['url'] = request.config.getoption('--url')
    config_param['status'] = request.config.getoption('--status_code')
    return config_param
