*** Settings ***
Resource    common.robot


*** Keywords ***
Page Should Contain Reference
    [Arguments]    ${type}    ${author}    ${title}    ${journal}    ${year}
    Bibtex Page Should Be Open
    Page Should Contain    ${type}
    Page Should Contain    ${author}
    Page Should Contain    ${title}
    Page Should Contain    ${journal}
    Page Should Contain    ${year}
