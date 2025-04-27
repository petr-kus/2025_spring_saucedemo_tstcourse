*** Settings ***
Documentation      A test suite for valid login.
Library            LoginPage.py
# Library            InventoryPage.py
Library            SeleniumLibrary

*** Test Cases ***
Login user
    Open Page   https://www.saucedemo.com/
    Is Correct Page
    Check Title
    User Name standard_user
    Password secret_sauce
    Click Login Button
    Is User Logged
    Close driver

Login user by selenium lib
    Open Browser  url=https://www.saucedemo.com/  browser=edge
    Input Text  user-name  standard_user
    Input Text  password  secret_sauce
    Click Button  login-button

Better login user by selenium
    Open Browser  url=https://www.saucedemo.com/  browser=chrome
    Another Login standard_user with secret_sauce

# jak zaimplementovat dalsi moduly(dalsi test case)? muze byt zde nebo v jinem robot souboru?? - zatim neslo, problemy s drivery, Keywords atd..
# Add Item to cart
#     Open Page   https://www.saucedemo.com/
#     Is Correct Page
#     Check Title
#     User Name standard_user
#     Password secret_sauce
#     Click Login Button
#     Is User Logged
#     Check product page
#     Add item to cart
#     Enter cart page
#     Close driver


*** Keywords ***
User Name ${username}
    Enter User Name  ${username}

Password ${password}
    Enter Password  ${password}

# possible way for more variables:
# Login ${username} with ${password}
#     Login User  ${username}  ${password}

Another login ${username} with ${password}
    Input Text  user-name  ${username}
    Input Text  password  ${password}
    Click Button  login-button
