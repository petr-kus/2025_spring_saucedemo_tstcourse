*** Settings ***
Library    SeleniumLibrary
Resource    ../pages/login_page.resource
Resource    ../pages/menu_page_logout.resource
Resource    ../variables/global_variables.resource

*** Test Cases ***
Úspěšné odhlášení
    Open Browser               ${URL}          ${BROWSER}
    Prihlas se                 ${USERNAME_OK}  ${PASSWORD_OK}
    Odhlášení z webu
    Ověř úspěšné přihlášení    ${URL}
    Close Browser

