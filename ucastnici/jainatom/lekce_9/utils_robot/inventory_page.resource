*** Settings ***
Documentation     Resource file for Inventory page
Library           SeleniumLibrary

*** Variables ***
${INVENTORY_URL}     https://www.saucedemo.com/inventory.html
${BROWSER}           Edge

*** Keywords ***
User Is Logged
    [Documentation]       Checks successful login by checking current page
    Location Should Be    ${INVENTORY_URL}