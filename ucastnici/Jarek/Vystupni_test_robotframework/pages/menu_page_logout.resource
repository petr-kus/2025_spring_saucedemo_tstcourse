*** Settings ***
Library        SeleniumLibrary

*** Variables ***
${MENU_BUTTON}            id=react-burger-menu-btn
${LOGOUT_BUTTON}          xpath=//a[text()='Logout']

*** Keywords ***
Otevřít menu
    Click Button    ${MENU_BUTTON}

Klikni na odhlášení
    Wait Until Element Is Visible    ${LOGOUT_BUTTON}     timeout=10s
    Click Element                   ${LOGOUT_BUTTON} 

Odhlášení z webu
    Otevřít menu
    Klikni na odhlášení



