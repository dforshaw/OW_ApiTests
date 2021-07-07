import requests
import json
import pytest
from tests.config import baseurl_value
from tests.config import appid_value


# Test Data
@pytest.mark.parametrize("city, state, country, expected", [
    ('Paris', '', '', 'Paris'),
    ('Paris', 'TX', 'US', 'Paris'),
    ('Castro Valley', '', '', 'Castro Valley')
])
def test_confirm_city_when_getting_weather_by_city_name(city, state, country, baseurl_value, appid_value, expected):
    parameters = {'q': city+','+state+','+country, 'appId': appid_value}
    response = requests.get(baseurl_value, params=parameters)

    info = json.loads(response.content)
    item = info['name']

    try:
        assert item == expected
    finally:
        print(info)
