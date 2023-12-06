*** Settings ***
Resource    common.robot


*** Keywords ***
Page Should Contain Reference
    [Arguments]    ${title}    ${author}    ${year}
    List Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}

Page Reference Count Should Be
    [Arguments]    ${count}
    List Page Should Be Open
    ${page_count} =    SeleniumLibrary.Get Element Count    xpath://tr[@class='reference-row']
    Should Be Equal As Integers    ${page_count}    ${count}
