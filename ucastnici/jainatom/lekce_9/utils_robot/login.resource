*** Settings ***
Documentation     Resource file for login.robot test containing keywords and variables
Library           SeleniumLibrary

*** Variables ***
${LOGIN_URL}         https://www.saucedemo.com/
${INVENTORY_URL}     https://www.saucedemo.com/inventory.html
${BROWSER}           Firefox
${USERNAME_INPUT}    id=user-name
${PASSWORD_INPUT}    id=password
${LOGIN_BUTTON}      id=login-button
${VALID_USERNAME}    standard_user
${VALID_PASSWORD}    secretsauce
${INVALID_USERNAME}  substandard_user
${INVALID_PASSWORD}  saucesecret

*** Keywords ***
Open Login Page
    [Documentation]    Opens browser to login page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Title Should Be    Login Page

Login ${user} with ${password}
    Input Text     ${USERNAME_INPUT}    ${user}
    Input Text     ${PASSWORD_INPUT}    ${password}
    Click Button   ${LOGIN_BUTTON}

Is User Logged
    Location Should Be    ${INVENTORY_URL}

