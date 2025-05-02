*** Settings ***
Library           SeleniumLibrary
Resource          Pages/LoginPage.resource
Resource          Pages/ProductPage.resource
Resource          Pages/MenuPage.resource

Test Setup        Open Browser To Login Page
Test Teardown     Close Browser

*** Variables ***

${USERNAME_STD}         standard_user
${PASSWORD_STD}         secret_sauce

${USERNAME_PRB}         problem_user
${PASSWORD_PRB}         secret_sauce

*** Test Cases ***
Reset App State Clears Cart As Standard User
    Log To Console    Test začal.
    Log In With Credentials    ${USERNAME_STD}    ${PASSWORD_STD}
    Add Product To Cart
    Go To Menu And Reset App State
    Cart Should Be Empty
    Check Product Button Is Add To Cart
    Check Product Button is possible to change
    Log To Console    Test skončil.
    
Reset App State Clears Cart As Problem User
    Log To Console    Test začal.
    Log In With Credentials    ${USERNAME_PRB}    ${PASSWORD_PRB}
    Add Product To Cart
    Go To Menu And Reset App State
    Cart Should Be Empty
    Check Product Button Is Add To Cart
    Check Product Button is possible to change
    Log To Console    Test skončil.