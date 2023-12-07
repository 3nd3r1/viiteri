*** Settings ***
Resource    common.robot


*** Keywords ***
View Table Page Should Contain Reference
    [Arguments]    ${title}    ${author}    ${year}
    View Table Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}

View Table Page Reference Count Should Be
    [Arguments]    ${count}
    View Table Page Should Be Open
    ${page_count} =    Get Element Count    xpath://tr[@class='reference-row']
    Should Be Equal As Integers    ${page_count}    ${count}

View Bibtex Page Should Contain Reference
    [Arguments]    ${reference_type}    ${title}    ${author}    ${year}
    View Bibtex Page Should Be Open
    ${textbox} =    Get Text    xpath://textarea[@id='textarea']
    Should Contain    ${textbox}    @${reference_type}{
    Should Contain    ${textbox}    title = "${title}"
    Should Contain    ${textbox}    author = "${author}"
    Should Contain    ${textbox}    year = "${year}"
