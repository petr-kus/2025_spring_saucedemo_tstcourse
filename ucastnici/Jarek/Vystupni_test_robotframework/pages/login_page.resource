*** Settings ***
Library    SeleniumLibrary
Resource    ../variables/global_variables.resource

*** Variables ***
${USERNAME_INPUT}         id=user-name
${PASSWORD_INPUT}         id=password
${LOGIN_BUTTON}           id=login-button

*** Keywords ***
Zadej uživatelské jméno
    [Arguments]    ${jmeno}
    Input Text    ${USERNAME_INPUT}    ${jmeno}

Zadej heslo
    [Arguments]     ${heslo}
    Input Text    ${PASSWORD_INPUT}    ${heslo}

Klikni na login
    Click Button    ${LOGIN_BUTTON}

Prihlas se
    [Arguments]    ${jmeno}    ${heslo}
    Zadej uživatelské jméno    ${jmeno}
    Zadej heslo                ${heslo}
    Klikni na login

Ověř úspěšné přihlášení
    [Arguments]    ${valid_url}
    Location Should Be    ${valid_url}

Kontrolní neúspěšné přihlášení
    [Arguments]    ${css_selector}
    Page Should Contain Element     ${css_selector}


