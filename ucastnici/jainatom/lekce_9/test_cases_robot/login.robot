*** Settings ***
Documentation     A test suite with positive and negative test scenarios.
...
...               Keywords are imported from the resource file
Resource          ..\utils_robot\login.resource
Resource          ..\saucedemo\LoginPage.py
Default Tags      positive

*** Test Cases ***
Login User with Password
    Given Open Login Page
    When Login ${VALID_USERNAME} with ${VALID_PASSWORD}
    Then Is User Logged
    [Teardown]    Close Browser

# Denied Login with Wrong Password
#     [Tags]    negative
#     Connect to Server
#     Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123
#     Verify Unauthorised Access
#     [Teardown]    Close Server Connection

# Denied Login with Wrong User and Existing Password
#     [Tags]    negative
#     Connect to Server
#     Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123
#     Verify Unauthorised Access
#     [Teardown]    Close Server Connection

# Denied Login with Wrong User and Wrong Password
#     [Tags]    negative
#     Connect to Server
#     Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123
#     Verify Unauthorised Access
#     [Teardown]    Close Server Connection