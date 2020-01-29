import pytest
import requests
from random import randint as rand


def test_jsonplaceholder(test_jsonplaceholder_url):
    '''Checking jsonplaceholder resources list '''
    response = requests.get(test_jsonplaceholder_url)
    result = response.json()
    assert result[0]['userId'] and result[0]['id'] and result[0]['title'] and result[0]['body'] and len(result) == 100


def test_jsonplaceholder_resource_creation(test_jsonplaceholder_url):
    '''Checking resource creation. The answer should be HTTP 201 Created '''

    data = {'title': 'otus', 'body': 'lesson 4', 'userId': 500}
    headers = {'Content-type': 'application/json; charset=UTF-8'}

    response = requests.post(test_jsonplaceholder_url, json=data, headers=headers)
    assert response.status_code == 201


@pytest.mark.parametrize('id', [str(rand(1, 100))])
def test_jsonplaceholder_random(test_jsonplaceholder_url, id):
    '''Checking jsonplaceholder random resource'''
    response = requests.get(test_jsonplaceholder_url + id)
    result = response.json()
    assert result['id'] == int(id)


@pytest.mark.parametrize('id', [str(100)])
def test_jsonplaceholder_resource_update(test_jsonplaceholder_url, id):
    '''Checking resource update. The answer should be HTTP 200 '''

    data = {'title': 'otus', 'body': 'Next lesson', 'userId': 500}
    headers = {'Content-type': 'application/json; charset=UTF-8'}

    response = requests.put(test_jsonplaceholder_url + id, json=data, headers=headers)
    assert response.status_code == 200


@pytest.mark.parametrize('id', [str(100)])
def test_jsonplaceholder_resource_delete(test_jsonplaceholder_url, id):
    '''Checking resource delete. The answer should be HTTP 200'''

    response = requests.delete(test_jsonplaceholder_url + id)
    assert response.status_code == 200
