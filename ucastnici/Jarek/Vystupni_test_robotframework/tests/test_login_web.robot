*** Settings ***
Library    SeleniumLibrary
Resource    ../pages/login_page.resource
Resource    ../variables/global_variables.resource

*** Test Cases ***
Úspěšné přihlášeni
    Open Browser               ${URL}          ${BROWSER}
    Prihlas se                 ${USERNAME_OK}  ${PASSWORD_OK}
    Ověř úspěšné přihlášení    ${URL_VALID}
    Close Browser

Neúspěšné přihlášeni
    Open Browser               ${URL}          ${BROWSER}
    Prihlas se                 ${USERNAME_NOK}  ${PASSWORD_NOK}
    Ověř úspěšné přihlášení    ${URL}
    Kontrolní neúspěšné přihlášení  ${CSS_ERROR_SELECTOR}
    Close Browser