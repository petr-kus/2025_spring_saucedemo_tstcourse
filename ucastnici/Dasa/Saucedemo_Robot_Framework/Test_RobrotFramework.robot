*** Settings ***
Documentation     Testy pro SauceDemo webovou aplikaci
Resource          resources/login_page.robot
Resource          resources/inventory_page.robot
Resource          resources/menu.robot
Library           SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${USERNAME}    standard_user
${PASSWORD}    secret_sauce

*** Keywords ***
Otevři Prohlížeč
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window

Zavři Prohlížeč
    Close Browser

*** Test Cases ***
Test Přihlášení Uživatele
    [Documentation]    Test přihlášení standardního uživatele
    [Setup]    Otevři Prohlížeč
    [Teardown]    Zavři Prohlížeč
    Vyplň Přihlašovací Údaje    ${USERNAME}    ${PASSWORD}
    Klikni Na Přihlásit
    Ověř Stránku S Produkty

Test Košík
    [Documentation]    Test přidání a odebrání produktů z košíku
    [Setup]    Otevři Prohlížeč
    [Teardown]    Zavři Prohlížeč
    Vyplň Přihlašovací Údaje    ${USERNAME}    ${PASSWORD}
    Klikni Na Přihlásit
    Ověř Stránku S Produkty
    Přidej Produkt Do Košíku    Sauce Labs Backpack
    Ověř Počet Produktů V Košíku    1
    Odeber Produkt Z Košíku    Sauce Labs Backpack
    Ověř Počet Produktů V Košíku    0

Test Odhlášení
    [Documentation]    Test odhlášení uživatele
    [Setup]    Otevři Prohlížeč
    [Teardown]    Zavři Prohlížeč
    Vyplň Přihlašovací Údaje    ${USERNAME}    ${PASSWORD}
    Klikni Na Přihlásit
    Ověř Stránku S Produkty
    Otevři Menu
    Klikni Na Odhlášení
    Ověř Přihlašovací Stránku
