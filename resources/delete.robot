*** Settings ***
Resource    common.robot


*** Keywords ***
Click Delete Reference
    [Arguments]    ${title}    ${author}    ${year}
    ${reference_row_locator} =    Set Variable
    ...    xpath://tr[contains(@class,'reference-row')]//td[text()='${title}']/following-sibling::td[text()='${author}']/following-sibling::td[text()='${year}']/..
    ${delete_button_locator} =    Set Variable
    ...    ${reference_row_locator}/following-sibling::tr[@class='button-row']//td//button[@class='delete-button']

    View Table Page Should Be Open

    Click Element    ${reference_row_locator}

    Click Element    ${delete_button_locator}
