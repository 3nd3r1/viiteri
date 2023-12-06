*** Settings ***
Library     SeleniumLibrary
Library     ../libraries/app_library.py


*** Variables ***
${SERVER}       localhost:5001
${DELAY}        0 seconds
${HOME_URL}     http://${SERVER}
${ADD_URL}      ${HOME_URL}/add
${VIEW_URL}     ${HOME_URL}/list


*** Keywords ***
Open And Configure Browser
    ${options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --headless
    Open Browser    browser=chrome    options=${options}
    Set Selenium Speed    ${DELAY}

Home Page Should Be Open
    Title Should Be    Home - Viiteri

Add Page Should Be Open
    Title Should Be    Submit - Viiteri

View Page Should Be Open
    Title Should Be    View - Viiteri

Go To Home Page
    Go To    ${HOME_URL}

Go To Add Page
    Go To    ${ADD_URL}

Go To View Page
    Go To    ${VIEW_URL}
