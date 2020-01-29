import json
import pytest
import requests
from jsonschema import validate
from random import randint as rand


def test_openbrewerydb(test_openbrewerydb_url):
    '''Checking https://api.openbrewerydb.org/breweries/ availability. Should be 200'''
    response = requests.get(test_openbrewerydb_url)
    assert response.status_code == 200


def test_openbrewerydb_json_schema(test_openbrewerydb_url):
    '''Response structure check'''
    response = requests.get(test_openbrewerydb_url)
    result = response.json()
    schema = {
        "type": "object",
        "properties": {
            'id': {'type': 'number'},
            'name': {'type': 'string'},
            'brewery_type': {'type': 'string'},
            'street': {'type': 'string'},
            'city': {'type': 'string'},
            'state': {'type': 'string'},
            'postal_code': {'type': 'string'},
            'country': {'type': 'string'},
            'longitude': {'type': 'string'},
            'latitude': {'type': 'string'},
            'phone': {'type': 'string'},
            'website_url': {'type': 'string'},
            'updated_at': {'type': 'string'},
            'tag_list': {'type': 'array'}
        },
        "required": ['id', 'name', 'brewery_type', 'street', 'city', 'state', 'postal_code', 'country', 'longitude',
                     'latitude', 'phone', 'website_url', 'updated_at', 'tag_list']
    }

    validate(instance=result[0], schema=schema)


@pytest.mark.parametrize('search', ['beer', 'gold', 'best', 'you', 'old'])
def test_openbrewerydb_search(test_openbrewerydb_url, search):
    '''Checking search requests. Should return list of dict containing keys id and name'''
    response = requests.get(test_openbrewerydb_url + '/' + 'autocomplete', params={'query': search})
    result = json.loads(response.text)
    assert result[0]['id'] and result[0]['name']


@pytest.mark.parametrize('id', [str(rand(1, 1000))])
def test_openbrewerydb_by_id(test_openbrewerydb_url, id):
    '''Checking random brewery id'''
    response = requests.get(test_openbrewerydb_url + '/' + id)
    result = json.loads(response.text)
    assert result['name']


@pytest.mark.parametrize('city', ['detroit', 'washington', 'new_york'])
def test_openbrewerydb_order(test_openbrewerydb_url, city):
    '''Checking sort of brewery by city and order them descendingly'''
    response = requests.get(test_openbrewerydb_url, params={('by_city', city), ('sort', '+name')})
    print(response.url)
    result = json.loads(response.text)
    assert result[0]['name'] < result[-1]['name']
