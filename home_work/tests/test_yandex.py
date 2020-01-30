import requests


def test_response(request_params):
    '''Checking url and response. For valid urls code should be 200, for invalid - 404 otherwise test will fail '''

    response = requests.get(request_params['url'])
    assert response.status_code == int(request_params['status'])
