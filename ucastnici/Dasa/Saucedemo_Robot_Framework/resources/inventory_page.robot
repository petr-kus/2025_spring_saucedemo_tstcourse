*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${INVENTORY_LIST}    class=inventory_list
${PRODUCT_ITEM}    class=inventory_item
${ADD_TO_CART_BUTTON}    xpath=//button[contains(@id, 'add-to-cart')]
${REMOVE_BUTTON}    xpath=//button[contains(@id, 'remove')]
${CART_BADGE}    class=shopping_cart_badge
${SORT_DROPDOWN}    class=product_sort_container

*** Keywords ***
Ověř Stránku S Produkty
    Wait Until Element Is Visible    ${INVENTORY_LIST}
    Page Should Contain Element    ${INVENTORY_LIST}

Přidej Produkt Do Košíku
    [Arguments]    ${product_name}
    Click Button    xpath=//div[text()='${product_name}']/ancestor::div[@class='inventory_item']//button[contains(@id, 'add-to-cart')]

Odeber Produkt Z Košíku
    [Arguments]    ${product_name}
    Click Button    xpath=//div[text()='${product_name}']/ancestor::div[@class='inventory_item']//button[contains(@id, 'remove')]

Ověř Počet Produktů V Košíku
    [Arguments]    ${expected_count}
    ${count}=    Get Element Count    ${CART_BADGE}
    Should Be Equal As Numbers    ${count}    ${expected_count}

Seřaď Produkty
    [Arguments]    ${option}
    Click Element    ${SORT_DROPDOWN}
    Click Element    xpath=//option[text()='${option}']

Ověř Seřazení Produktů
    [Arguments]    ${option}
    Element Should Be Visible    xpath=//option[text()='${option}' and @selected='selected'] 