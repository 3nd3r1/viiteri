*** Settings ***
Resource            ../../resources/common.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Add Article Page


*** Test Cases ***
Add Article Successfully
    Set Author  Pekka Mikkola
    Set Title  Maijan artikkeli
    Set Journal  Maijan artikkelikokoelma
    Set Year  2011
    Submit Article Reference
    Add Article Should Succeed

# Add Article Unsuccessfully
#     Set Author  Pekka Mikkola
#     Set Title  Maijan artikkeli
#     Set Journal  Maijan artikkelikokoelma
#     Submit Article Reference
#     Should Fail With Message  Please fill in this field.

*** Keywords ***
Add Article Should Succeed
    Add Page Should Be Open

# Should Fail With Message
#     [Arguments]  ${message}
#     Page Should Contain  ${message}

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

Submit Article Reference
    Click Button    Submit article

Go To Add Article Page
    Go To Add Page
    Add Page Should Be Open
