*** Settings ***
Resource    common.robot
Resource    view.robot


*** Keywords ***
Get Delete Button Locator
    [Arguments]    ${title}    ${author}    ${year}
    ${reference_row_locator} =    Get Reference Row Locator    ${title}    ${author}    ${year}
    ${delete_button_locator} =    Set Variable
    ...    ${reference_row_locator}//td//table//tbody//tr//td//div//form//input[@class="button delete-button"]
    RETURN    ${delete_button_locator}

Click Delete Reference
    [Arguments]    ${title}    ${author}    ${year}
    ${delete_button_locator} =    Get Delete Button Locator    ${title}    ${author}    ${year}

    View Table Page Should Be Open

    Click Reference    ${title}    ${author}    ${year}
    Click Element    ${delete_button_locator}

Reference Deletion Should Be Confirmed
    Notification should be visible with message and type    Reference removed successfully!    success
