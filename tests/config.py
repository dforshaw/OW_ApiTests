import pytest


@pytest.fixture
def baseurl_value():
    baseurl = 'https://api.openweathermap.org/data/2.5/weather'
    return baseurl


@pytest.fixture
def appid_value():
    appid = '21f40765a37081dd79daea2d68d09de9'
    return appid
