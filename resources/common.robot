*** Settings ***
Library     SeleniumLibrary
Library     ../libraries/ReferenceRepositoryLibrary.py


*** Variables ***
${SERVER}               localhost:5001
${DELAY}                0 seconds
${HOME_URL}             http://${SERVER}
${ADD_URL}              ${HOME_URL}/add
${SEARCH_URL}       ${HOME_URL}/list
${RAW_BIBTEX_URL}      ${HOME_URL}/bibtex


*** Keywords ***
Open And Configure Browser
    ${options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --headless
    Open Browser    browser=chrome    options=${options}
    Set Selenium Speed    ${DELAY}

Notification should be visible with message and type
    [Documentation]    Checks that a notification is visible with given message and type
    [Arguments]    ${message}    ${type}
    Wait Until Element is Visible    class:alert
    Element Should Be Visible    class:alert
    Element Text Should Be    class:alert    ${message}
    Element Attribute Value Should Be    class:alert    class    alert ${type}

Reference Count In Database Should Be
    [Arguments]    ${count}
    ${database_count}    Get Reference Count In Database
    Should Be Equal As Integers    ${count}    ${database_count}

Home Page Should Be Open
    Title Should Be    Home - Viiteri

Add Page Should Be Open
    Title Should Be    Submit - Viiteri

Search Page Should Be Open
    Title Should Be    Search - Viiteri

Raw BibTex Page Should Be Open
    Title Should Be    Raw BibTex - Viiteri

Go To Home Page
    Go To    ${HOME_URL}

Go To Add Page
    Go To    ${ADD_URL}

Go To Search Page
    Go To    ${SEARCH_URL}

Go To Raw BibTex Page
    Go To    ${RAW_BIBTEX_URL}
