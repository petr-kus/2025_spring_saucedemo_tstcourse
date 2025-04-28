*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${PRODUCT_NAME}         Sauce Labs Backpack
${PRODUCT_BUTTON}       xpath=//button[contains(@id, 'sauce-labs-backpack')]

*** Keywords ***
Add Product To Cart
    Click Button    xpath=//div[text()='${PRODUCT_NAME}']/ancestor::div[@class='inventory_item']//button

Cart Should Be Empty
    Page Should Not Contain Element    span.shopping_cart_badge

Check Product Button Is Add To Cart
    ${button_text}=    Get Text    ${PRODUCT_BUTTON}
    Run Keyword If    '${button_text}' == 'Remove'    Show Alert    ${button_text}
    Run Keyword If    '${button_text}' == 'Add to cart'    Should Be Equal    ${button_text}    Add to cart

Show Alert
    [Arguments]    ${message}
    Log    ALERT: ${message}

Check Product Button is possible to change
    ${button_text}=    Get Text    ${PRODUCT_BUTTON}
    Run Keyword If    '${button_text}' == 'Remove'    Click Button    ${PRODUCT_BUTTON}
    ${new_button_text}=    Get Text    ${PRODUCT_BUTTON}
    Run Keyword If    '${new_button_text}' == 'Remove'    Fail    Button should have changed to 'Add to cart'
    Run Keyword If    '${new_button_text}' == 'Add to cart'    Log    Button changed to 'Add to cart'