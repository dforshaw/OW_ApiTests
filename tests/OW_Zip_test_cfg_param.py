import requests
import json
import pytest
from tests.config import baseurl_value
from tests.config import appid_value


# Test Data
@pytest.mark.parametrize("zipCode, countryCode, expected", [
    ('94552', '', 'Castro Valley'),
    ('43140', '', 'London'),
    ('94040', '', 'Mountain View'),
    ('10007', '', 'New York'),
])
def test_confirm_city_when_getting_weather_by_zip(zipCode, countryCode, baseurl_value, appid_value, expected):
    parameters = {'zip': zipCode+','+countryCode, 'appId': appid_value}
    response = requests.get(baseurl_value, params=parameters)

    info = json.loads(response.content)
    itemName = info['name']

    try:
        assert itemName == expected
    finally:
        print(info)
