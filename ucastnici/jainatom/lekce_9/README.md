# Final assignment for 2025 spring test course
Test cases for [saucedemo](https://www.saucedemo.com) in Pytest and Robot Framework. Currently only serving tests for login, but everyone has to start somewhere.
==============================
## Project Structure
-------------
### Pytest
-----------------
* utils_pytest        - useful functions
* saucedemo           - POM objects
* test_cases_pytest   - test cases
* assets              - style.css file; I forgot what I use it for
* env_variables       - currently only declaring login page url

### Robot Framework
-----------------
* utils_robot               -settings, variables and keywords definitions
* test_cases_robot

## Requirements
* Python 3.11+
* Pytest
* Robot Framework

## Setup Instructions for Windows
```bash
py -m venv.venv
.venv/Scripts/activate
```
select Python interpreter and then:
```bash
pip install -r requirements.txt
```

## Running Tests
-------------
### Pytest
To run all test cases in test file (test_login_v3.py):
```bash
pytest .\test_login_v3.py 
```

### Robot Framework
To run all test cases in test file (login.robot):
```bash
robot .\login.robot 
```

## Outputs
-------------
### Pytest
* <test_case_name>_report.html

### Robot Framework
* log.html
* output.xml - I find this one the most useful for looking up the cause of what went wrong.
* report.html
* screenshots

