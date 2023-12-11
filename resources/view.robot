*** Settings ***
Resource    common.robot


*** Keywords ***
View Table Page Should Contain Reference
    [Arguments]    ${title}    ${author}    ${year}
    View Table Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}

View Table Page Should Contain Extended Reference Details
    [Documentation]    View Table näkymän refaktorointi #106

    [Arguments]    ${title}    ${author}    ${year}    ${journal}    ${detailsbutton}    ${deletebutton}
    View Table Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}
    Page Should Contain    ${journal}
    Page Should Contain Element    ${detailsbutton}
    Page Should Contain Element    ${deletebutton}

View Table Page Reference Count Should Be
    [Arguments]    ${count}
    View Table Page Should Be Open
    ${page_count} =    Get Element Count    xpath://tr[@class='reference-row']
    Should Be Equal As Integers    ${page_count}    ${count}

View Bibtex Page Should Contain Reference
    [Arguments]    ${reference_type}    ${title}    ${author}    ${year}
    View Bibtex Page Should Be Open
    ${textbox} =    Get Text    xpath://textarea[@id='textarea']
    Container Should Contain Reference In Bibtex    ${textbox}    ${reference_type}    ${title}    ${author}    ${year}

Click Copy All To Clipboard Button
    View BibTex Page Should Be Open

    Click Element    xpath://button[@id='copy-button']

# Clipboard Should Contain Reference
#    [Arguments]    ${reference_type}    ${title}    ${author}    ${year}
#    ${clipboard} =    Get Clipboard Value
#
#    Container Should Contain Reference In Bibtex
#    ...    ${clipboard}
#    ...    ${reference_type}
#    ...    ${title}
#    ...    ${author}
#    ...    ${year}

Container Should Contain Reference In Bibtex
    [Arguments]    ${container}    ${reference_type}    ${title}    ${author}    ${year}
    Should Contain    ${container}    @${reference_type}{
    Should Contain    ${container}    title = "${title}"
    Should Contain    ${container}    author = "${author}"
    Should Contain    ${container}    year = "${year}"
