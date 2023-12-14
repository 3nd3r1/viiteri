*** Settings ***
Resource    common.robot


*** Keywords ***
# View Table Keywords -----------------------------------------------------------

View Table Page Should Contain Reference
    [Arguments]    ${title}    ${author}    ${year}
    View Table Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}

View Table Page Should Contain Extended Reference Details With Fields
    [Arguments]    &{fields}
    View Table Page Should Be Open
    FOR    ${field_value_tuple}    IN    &{fields}
        View Table Page Should Contain Reference Details Row With    ${field_value_tuple}[0]    ${field_value_tuple}[1]
    END

View Table Page Should Contain Reference Details Row With
    [Arguments]    ${field}    ${value}
    ${detail_row_locator} =    Set Variable    xpath://tr[starts-with(@class,'reference-details')]
    Page Should Contain Element    ${detail_row_locator}//td[@class='reference-details-labels' and text()='${field}']
    Page Should Contain Element    ${detail_row_locator}//td[@class='reference-details-values' and text()='${value}']

View Table Page Reference Count Should Be
    [Arguments]    ${count}
    View Table Page Should Be Open
    ${page_count} =    Get Element Count    xpath://tr[@class='reference-row']
    Should Be Equal As Integers    ${page_count}    ${count}

Get Reference Row Locator
    [Arguments]    ${title}    ${author}    ${year}
    ${reference_row_locator} =    Set Variable
    ...    xpath://tr[contains(@class,'reference-row') and @data-title='${title}' and @data-author='${author}' and @data-year='${year}']
    RETURN    ${reference_row_locator}

Click Reference
    [Arguments]    ${title}    ${author}    ${year}
    ${reference_row_locator} =    Get Reference Row Locator    ${title}    ${author}    ${year}

    View Table Page Should Be Open

    Wait Until Element Is Visible    ${reference_row_locator}
    Wait Until Element Is Enabled    ${reference_row_locator}
    Click Element    ${reference_row_locator}

# View BibTex Keywords ----------------------------------------------------------

View Bibtex Page Should Contain Reference
    [Arguments]    ${reference_type}    ${title}    ${author}    ${year}
    View Bibtex Page Should Be Open
    ${textbox} =    Get Text    xpath://pre[@id='bibtex-output']
    Container Should Contain Reference In Bibtex    ${textbox}    ${reference_type}    ${title}    ${author}    ${year}

Container Should Contain Reference In Bibtex
    [Arguments]    ${container}    ${reference_type}    ${title}    ${author}    ${year}
    Should Contain    ${container}    @${reference_type}{
    Should Contain    ${container}    title = "${title}"
    Should Contain    ${container}    author = "${author}"
    Should Contain    ${container}    year = ${year}
