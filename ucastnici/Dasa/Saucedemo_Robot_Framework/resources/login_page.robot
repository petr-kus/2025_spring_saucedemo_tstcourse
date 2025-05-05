*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}    https://www.saucedemo.com
${USERNAME_FIELD}    id=user-name
${PASSWORD_FIELD}    id=password
${LOGIN_BUTTON}    id=login-button
${ERROR_MESSAGE}    class=error-message-container

*** Keywords ***
Otevři Přihlašovací Stránku
    Go To    ${LOGIN_URL}

Vyplň Přihlašovací Údaje
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Password    ${PASSWORD_FIELD}    ${password}

Klikni Na Přihlásit
    Click Button    ${LOGIN_BUTTON}

Ověř Chybovou Hlášku
    [Arguments]    ${expected_message}
    Element Should Be Visible    ${ERROR_MESSAGE}
    Element Should Contain    ${ERROR_MESSAGE}    ${expected_message}

Ověř Přihlašovací Stránku
    Element Should Be Visible    ${LOGIN_BUTTON}
    Page Should Contain Element    ${USERNAME_FIELD}
    Page Should Contain Element    ${PASSWORD_FIELD} 