*** Settings ***
Resource    common.robot


*** Keywords ***
Page Should Contain Reference
    [Arguments]    ${title}    ${author}    ${year}
    List Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}

Page Should Contain Whole Reference
    [Arguments]    ${journal}
    List Page Should Be Open
    Page Should Contain    ${journal}

Page Reference Count Should Be
    [Arguments]    ${count}
    List Page Should Be Open
    ${page_count} =    SeleniumLibrary.Get Element Count    xpath://tr[@class='reference-row']
    Should Be Equal As Integers    ${page_count}    ${count}

View Whole Reference
    ${row} =    Get WebElement    xpath://tbody/tr[@class='reference-row']/td[1]
    Click Element    ${row}
