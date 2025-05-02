*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${REMOVE_BUTTON}      xpath=//button[starts-with(@id, 'remove')]
*** Keywords ***
Náhodně přidej produkt do košíku
    ${PRODUKTY}               Get WebElements    xpath=//button[starts-with(@id, 'add-to-cart-')]
    ${POCET}                  Get Length         ${PRODUKTY}
    ${INDEX}                  Evaluate           random.randint(0, ${POCET} - 1)    modules=random
    Click Element   ${PRODUKTY}[${INDEX}]

Přidej jeden produkt do košíku
    ${PRODUKTY}               Get WebElements    xpath=//button[starts-with(@id, 'add-to-cart-')]
    Click Element   ${PRODUKTY}[${1}]

Zkontroluj počet položek v košíku
    ${text}     Get Text    css=.shopping_cart_badge
    ${pocet_polozek_kosik}    Convert To Integer  ${text}
    ${pocet_tlacitek_remove}    Get Element Count    ${REMOVE_BUTTON}
    Should Be Equal As Integers    ${pocet_tlacitek_remove}    ${pocet_polozek_kosik}  Počet tlačítek REMOVE (${pocet_tlacitek_remove}) nesouhlasí s badge (${pocet_polozek_kosik})!
    Log To Console    Počet položek v košíku je: ${pocet_polozek_kosik}   Počet tlačítek REMOVE je: ${pocet_tlacitek_remove}

Odeber všechny produkty z košíku
    ${pocet}    Get Element Count    ${REMOVE_BUTTON}

    WHILE    ${pocet} > 0 
        ${produkty}    Get WebElements    ${REMOVE_BUTTON}
        Click Element    ${produkty}[0]
        ${pocet}    Get Element Count   ${REMOVE_BUTTON}
    END


    