*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${MENU_BUTTON}          id=react-burger-menu-btn
${RESET_LINK}           id=reset_sidebar_link

*** Keywords ***
Go To Menu And Reset App State
    Click Button    ${MENU_BUTTON}
    Wait Until Element Is Visible    ${RESET_LINK}
    Click Element   ${RESET_LINK}
