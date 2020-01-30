import pytest
import requests
from jsonschema import validate


def test_dog(test_dog_url):
    '''Checking https://dog.ceo/dog-api/ availability. Should be 200'''
    response = requests.request('GET', test_dog_url)
    assert response.status_code == 200


def test_dog_json_schema():
    '''Response structure check'''
    response = requests.post('https://dog.ceo/api/breed/hound/list')

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }

    validate(instance=response.json(), schema=schema)


def test_dog_random_mult_img():
    '''Response should contain jpg file'''
    response = requests.get('https://dog.ceo/api/breeds/image/random/')
    parsed_data = response.text

    assert parsed_data.count('.jpg') == 1


@pytest.mark.parametrize('multi', ['1', '10', '49', '50'])
def test_dog_random_mult_img_positive(multi):
    '''Response should contain as many jpgs as given. Sometimes test can fail, because answer contain less items, thet requested by 1 paint'''

    response = requests.get('https://dog.ceo/api/breeds/image/random/' + multi)
    parsed_data = response.text
    assert parsed_data.count('.jpg') == int(multi)


@pytest.mark.parametrize('multi', ['51', '100'])
def test_dog_random_mult_img_negative(multi):
    '''Response should contain 50 jpgs. Sometimes test can fail, because answer contain less items, thet requested by 1 paint'''

    response = requests.get('https://dog.ceo/api/breeds/image/random/' + multi)
    parsed_data = response.text
    assert parsed_data.count('.jpg') == 50


@pytest.mark.parametrize('breed', ["afghan", "basset", "blood", "english", "ibizan", "walker"])
def test_dog_sub_breed_img(breed):
    '''Response should contain individual path for each breed'''

    response = requests.get('https://dog.ceo/api/breed/hound/' + breed + '/images')
    parsed_data = response.text
    assert parsed_data.count('.jpg') > 0
    assert parsed_data.count('hound-' + breed) > 0
