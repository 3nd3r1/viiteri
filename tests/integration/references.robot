*** Settings ***
Resource            ../../resources/common.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Add Reference Page

Library    XML

*** Test Cases ***
Add Article Successfully
    Select From List By Value  form_select  article
    Set Author  Pekka Mikkola  article
    Set Title  Maijan artikkeli  article
    Set Journal  Maijan artikkelikokoelma  article
    Set Year  2011  article
    Submit Reference
    Add Reference Should Succeed

Add Book Successfully
    Select From List By Value  form_select  book
    Set Author  Maija  book
    Set Title  Maijan kirja  book
    Set Publisher  WSOY  book
    Set Year  2000  book
    Submit Reference
    Add Reference Should Succeed

# Add Article Unsuccessfully
#     Set Author  Pekka Mikkola
#     Set Title  Maijan artikkeli
#     Set Journal  Maijan artikkelikokoelma
#     Submit Article Reference
#     Should Fail With Alert  Please fill in this field.
#     # ^ ei toimi koska ei oo message vaan joku message box tai alert

*** Keywords ***
Add Reference Should Succeed
    Add Page Should Be Open
    Page Should Contain    Reference created successfully!

# Should Fail With Alert
#     [Arguments]  ${message}
#     Alert Should Be Present  ${message}

Find Correct Input
    [Arguments]  ${div_locator}  ${input_locator}
    ${input} =  Get WebElement  ${div_locator} >> xpath://input[@name='${input_locator}']
    Wait Until Element Is Enabled  ${input}
    [Return]  ${input}

Set Author
    [Arguments]  ${author}  ${div_id}
    ${input} =  Find Correct Input  ${div_id}  author
    Input Text  ${input}  ${author}

Set Title
    [Arguments]  ${title}  ${div_id}
    ${input} =  Find Correct Input  ${div_id}  title
    Input Text  ${input}  ${title}

Set Journal
    [Arguments]  ${journal}  ${div_id}
    ${input} =  Find Correct Input  ${div_id}  journal
    Input Text  ${input}  ${journal}

Set Year
    [Arguments]  ${year}  ${div_id}
    ${input} =  Find Correct Input  ${div_id}  year
    Input Text  ${input}  ${year}

Set Publisher
    [Arguments]  ${publisher}  ${div_id}
    ${input} =  Find Correct Input  ${div_id}  publisher
    Input Text  ${input}  ${publisher}

Submit Reference
    Click Button    Submit reference

Go To Add Reference Page
    Go To Add Page
    Add Page Should Be Open
