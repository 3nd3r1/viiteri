*** Settings ***
Resource            ../../resources/common.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Add Reference Page


*** Test Cases ***
Add Article Successfully
    Select From List By Value  form_select  article
    Set Author  Pekka Mikkola
    Set Title  Maijan artikkeli
    Set Journal  Maijan artikkelikokoelma
    Set Year  2011
    Submit Reference
    Add Reference Should Succeed

# Add Book Successfully
#     Select From List By Value  form_select  book
#     Set Author  Maija   <-  ei löydä kenttää, koittaa ehkä inputtaa articleen joka on piilotettu?
#     Set Title  Maijan kirja
#     Set Publisher  WSOY
#     Set Year  2000
#     Submit Reference
#     Add Reference Should Succeed

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
    Page Should Contain  Reference created successfully!

# Should Fail With Alert
#     [Arguments]  ${message}
#     Alert Should Be Present  ${message}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Submit Reference
    Click Button    Submit reference

Go To Add Reference Page
    Go To Add Page
    Add Page Should Be Open
