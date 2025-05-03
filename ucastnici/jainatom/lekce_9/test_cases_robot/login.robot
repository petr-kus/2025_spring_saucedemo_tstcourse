*** Settings ***
Documentation     A test suite with positive and negative test scenarios.
...
...               Keywords are imported from the resource file
Resource          ../utils_robot/login.resource
Default Tags      positive

*** Test Cases ***
Login User with Password
    Open Login Page
    Login ${VALID_USERNAME} with ${VALID_PASSWORD}
    User Is Logged
    Close Browser

Denied Login with Wrong Password
    [Tags]    negative
    Open Login Page
    Login ${VALID_USERNAME} with ${INVALID_PASSWORD}
    Run Keyword And Expect Error  ${INVALID_LOGIN_ERROR_MESSAGE}  User Is Logged
    Close Browser

Denied Login with Wrong User and Existing Password
    [Tags]    negative
    Open Login Page
    Login ${INVALID_USERNAME} with ${VALID_PASSWORD}
    Run Keyword And Expect Error  ${INVALID_LOGIN_ERROR_MESSAGE}  User Is Logged
    Close Browser

Denied Login with Wrong User and Wrong Password
    [Tags]    negative
    Open Login Page
    Login ${INVALID_USERNAME} with ${INVALID_PASSWORD}
    Run Keyword And Expect Error  ${INVALID_LOGIN_ERROR_MESSAGE}  User Is Logged
    Close Browser