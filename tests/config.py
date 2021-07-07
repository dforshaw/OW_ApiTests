import pytest


@pytest.fixture
def baseurl_value():
    baseurl = 'https://api.openweathermap.org/data/2.5/weather'
    return baseurl


@pytest.fixture
def appid_value():
    appid = '<Enter OPEN WEATHER API ID here>'
    return appid
