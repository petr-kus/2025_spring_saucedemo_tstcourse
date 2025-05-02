*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}                FireFox
${URL}                    https://www.saucedemo.com/
${URL_VALID}              https://www.saucedemo.com/inventory.html
${CSS_ERROR_SELECTOR}     css=h3[data-test="error"]

${USERNAME_OK}            standard_user
${PASSWORD_OK}            secret_sauce

${USERNAME_NOK}           locked_out_user
${PASSWORD_NOK}           secret_sauce



