*** Settings ***
Documentation     Resource file for login.robot test containing keywords and variables
Library           SeleniumLibrary

*** Variables ***
${LOGIN_URL}         https://www.saucedemo.com/
${INVENTORY_URL}     https://www.saucedemo.com/inventory.html
${BROWSER}           Edge
${USERNAME_INPUT}    id=user-name
${PASSWORD_INPUT}    id=password
${LOGIN_BUTTON}      id=login-button
${VALID_USERNAME}    standard_user
${VALID_PASSWORD}    secret_sauce
${INVALID_USERNAME}  substandard_user
${INVALID_PASSWORD}  sauce_secret
${INVALID_LOGIN_ERROR_MESSAGE}  Location should have been 'https://www.saucedemo.com/inventory.html' but was 'https://www.saucedemo.com/'.

*** Keywords ***
Open Login Page
    [Documentation]    Opens browser to login page
    Open Browser       ${LOGIN_URL}    ${BROWSER}
    Title Should Be    Swag Labs

Login ${user} with ${password}
    [Documentation]  Enters username and password and clicks on login button
    Input Text       ${USERNAME_INPUT}    ${user}
    Input Text       ${PASSWORD_INPUT}    ${password}
    Click Button     ${LOGIN_BUTTON}

User Is Logged
    [Documentation]       Checks successful login by checking current page
    Location Should Be    ${INVENTORY_URL}


    

