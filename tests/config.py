import pytest


# All API calls fall under the Base URL
@pytest.fixture
def baseurl_value():
    baseurl = 'https://api.openweathermap.org/data/2.5/weather'
    return baseurl


# Register for Open Weather API ID at https://openweathermap.org/current
@pytest.fixture
def appid_value():
    appid = '<Enter OPEN WEATHER API ID here>'
    return appid
