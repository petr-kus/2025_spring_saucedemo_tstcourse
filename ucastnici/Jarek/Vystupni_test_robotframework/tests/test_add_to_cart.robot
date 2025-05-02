*** Settings ***
Library    SeleniumLibrary
Resource    ../pages/login_page.resource
Resource    ../pages/inventory_page.resource
Resource    ../variables/global_variables.resource

*** Test Cases ***
Přidej náhodná produkt do košíku
    Open Browser               ${URL}          ${BROWSER}
    Prihlas se                 ${USERNAME_OK}  ${PASSWORD_OK}
    Ověř úspěšné přihlášení    ${URL_VALID}

    Náhodně přidej produkt do košíku
    Zkontroluj počet položek v košíku
    Odeber všechny produkty z košíku

    Přidej jeden produkt do košíku
    Zkontroluj počet položek v košíku
    Odeber všechny produkty z košíku

    Close Browser
    