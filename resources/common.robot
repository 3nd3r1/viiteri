*** Settings ***
Library     SeleniumLibrary
Library     ../libraries/app_library.py


*** Variables ***
${SERVER}       localhost:5001
${DELAY}        0 seconds
${HOME_URL}     http://${SERVER}


*** Keywords ***
Open And Configure Browser
    ${options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --headless
    Open Browser    browser=chrome    options=${options}
    Set Selenium Speed    ${DELAY}

Home Page Should Be Open
    Title Should Be    Etusivu - Viiteri

Go To Home Page
    Go To    ${HOME_URL}
