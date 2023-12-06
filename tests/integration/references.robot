*** Settings ***
Resource            ../../resources/common.robot
Library             XML
Library             Dialogs

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Home Page


*** Test Cases ***
Click Home Link
    Go To Home Page
    Home Page Should Be Open

Click Submit Link
    Go To Add Page
    Add Page Should Be Open

Click View Link
    Go To View Page
    View Page Should Be Open

Add Article Successfully
    Go To Add Page
    Check Reference Type    article
    Select From List By Value    form_select    article
    Set Author    Pekka Mikkola    article
    Set Title    Maijan artikkeli    article
    Set Journal    Maijan artikkelikokoelma    article
    Set Year    2011    article
    Submit Reference    article
    Add Reference Should Succeed

Add Book Successfully
    Go To Add Page
    Check Reference Type    article
    Select From List By Value    form_select    book
    Set Author    Maija Makkonen    book
    Set Title    Maijan kirja    book
    Set Publisher    WSOY    book
    Set Year    2000    book
    Submit Reference    book
    Add Reference Should Succeed

Add Inproceedings Successfully
    Go To Add Page
    Check Reference Type    book
    Select From List By Value    form_select    inproceedings
    Set Author    Maija    inproceedings
    Set Title    Maijan inproceedings    inproceedings
    Set Booktitle    Maijan kokoelma    inproceedings
    Set Year    2011    inproceedings
    Submit Reference    inproceedings
    Add Reference Should Succeed

Add Two References Consecutively
    Go To Add Page
    Check Reference Type    inproceedings
    Select From List By Value    form_select    article
    Set Author    Pekka Mikkola    article
    Set Title    Maijan artikkeli    article
    Set Journal    Maijan artikkelikokoelma    article
    Set Year    2011    article
    Submit Reference    article
    Add Reference Should Succeed
    Click Button    Submit another reference
    Check Reference Type    article
    Select From List By Value    form_select    book
    Set Author    Maija Makkonen    book
    Set Title    Maijan kirja    book
    Set Publisher    WSOY    book
    Set Year    2000    book
    Submit Reference    book
    Add Reference Should Succeed

View All Added References
    Go To View Page
    Page Should Contain    Pekka Mikkola
    Page Should Contain    Maijan artikkeli
    Page Should Contain    2011
    ${count} =    SeleniumLibrary.Get Element Count    xpath://tr[@class='reference-row']
    # Oletuksena countille, että tietokanta on tyhjä ja lasketaan hr-elementit
    # aiempien test casejen lisäämien viitteiden perusteella
    Should Be Equal As Integers    ${count}    5

Add Article Unsuccessfully
    Go To Add Page
    Check Reference Type    book
    Select From List By Value    form_select    article
    Set Author    Pekka Mikkola    article
    Set Title    Maijan artikkeli    article
    Set Journal    Maijan artikkelikokoelma    article
    Submit Reference    article
    ${error} =    SeleniumLibrary.Get Element Attribute
    ...    xpath://div[@id='article']//input[@name='year']
    ...    validationMessage
    Should Not Be Empty    ${error}


*** Keywords ***
Add Reference Should Succeed
    Add Page Should Be Open
    Page Should Contain    Reference created successfully!

Check Reference Type
    # Tarkistaa, että sessio tallentaa viitteen tyypin onnistuneesti
    [Arguments]    ${type}
    ${select} =    Get WebElement    form_select
    ${selected} =    Get Selected List Value    ${select}
    Should Be Equal As Strings    ${selected}    ${type}

Find Correct Input
    [Arguments]    ${div_locator}    ${input_locator}
    ${input} =    Get WebElement    xpath://div[@id='${div_locator}']//input[@name='${input_locator}']
    Wait Until Element Is Enabled    ${input}
    Wait Until Element Is Visible    ${input}
    RETURN    ${input}

Set Author
    [Arguments]    ${author}    ${div_locator}
    ${input} =    Find Correct Input    ${div_locator}    author
    Input Text    ${input}    ${author}

Set Title
    [Arguments]    ${title}    ${div_locator}
    ${input} =    Find Correct Input    ${div_locator}    title
    Input Text    ${input}    ${title}

Set Journal
    [Arguments]    ${journal}    ${div_locator}
    ${input} =    Find Correct Input    ${div_locator}    journal
    Input Text    ${input}    ${journal}

Set Year
    [Arguments]    ${year}    ${div_locator}
    ${input} =    Find Correct Input    ${div_locator}    year
    Input Text    ${input}    ${year}

Set Publisher
    [Arguments]    ${publisher}    ${div_locator}
    ${input} =    Find Correct Input    ${div_locator}    publisher
    Input Text    ${input}    ${publisher}

Set Booktitle
    [Arguments]    ${booktitle}    ${div_locator}
    ${input} =    Find Correct Input    ${div_locator}    booktitle
    Input Text    ${input}    ${booktitle}

Submit Reference
    [Arguments]    ${div_locator}
    Click Button    xpath://div[@id='${div_locator}']//button
