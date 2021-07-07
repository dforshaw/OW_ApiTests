import requests
import json
import pytest
from tests.config import baseurl_value
from tests.config import appid_value


# Test Data
@pytest.mark.parametrize("lon, lat, expected", [
    ('-122.0863', '37.6941', 'Castro Valley'),
    ('-96.7836', '32.7668', 'Dallas'),
])
def test_confirm_lon_lat_when_getting_weather_by_lon_lat(lon, lat, baseurl_value, appid_value, expected):
    parameters = {'lon': lon, 'lat': lat, 'appId': appid_value}
    response = requests.get(baseurl_value, params=parameters)

    info = json.loads(response.content)
    itemName = info['name']
    itemLon = info['coord']['lon']
    itemLat = info['coord']['lat']

    try:
        assert itemLon == float(lon)
        assert itemLat == float(lat)
        assert itemName == expected
    finally:
        print(info)
