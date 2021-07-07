# API Test Framework for Validating Open Weather API

#### Purpose
This test suite includes basic validation of three (3) of the [Open Weather API](https://openweathermap.org/current) queries
- Obtain the Current Weather By City
- Obtain the Current Weather By Latitude & Longitude
- Obtain the Current Weather By Zip Code

#### Environment
- Python 3 should be installed
- Clone the repository to your local environment
- Create a virtual environment in the local project folder
- Install the needed support packages
    - pip install -r requirements.txt

#### Data
- Sign up for an [Open Weather API](https://openweathermap.org/current) appId to execute the tests
  - Update config.py with your appId
- Review the parametrize decorator & the listed data values 
    - Add/edit input values & expected results you wish to validate with

#### Run Options
###### Test Runner: pytest
- To run all tests in the test suite:
  - pytest tests/*
- To run a specific test in the test suite:
  - pytest tests/<test_case>.py

#### Reporting
###### Test Reports: pytest-html
- To view a report of the test run:
  - pytest tests/* -v --html report.html
- Click the specific test case in the report to view errors
    
