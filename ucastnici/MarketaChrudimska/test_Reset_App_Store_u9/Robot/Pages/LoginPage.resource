*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    Edge
${USERNAME_FIELD}    id=user-name
${PASSWORD_FIELD}    id=password
${LOGIN_BUTTON}      id=login-button

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Page Contains Element    ${USERNAME_FIELD}

Log In With Credentials
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}
    Click Button  ${LOGIN_BUTTON}
    Wait Until Page Contains Element    class=inventory_list