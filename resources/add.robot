*** Settings ***
Resource    common.robot


*** Keywords ***
Reference Addition Should Be Confirmed
    Notification should be visible with message and type    Reference created successfully!    success

Reference Addition Should Be Rejected With Message
    [Arguments]    ${message}
    Notification should be visible with message and type    ${message}    error

Reference Addition Should Be Rejected With Invalid Field
    [Arguments]    ${reference_type}    ${field_name}
    ${error} =    SeleniumLibrary.Get Element Attribute
    ...    xpath://div[@id='${reference_type}']//input[@name='${field_name}']
    ...    validationMessage
    Should Not Be Empty    ${error}

Select Reference Type
    [Arguments]    ${reference_type}
    Select From List By Value    form_select    ${reference_type}

Selected Reference Type Should Be
    [Arguments]    ${reference_type}
    ${current_reference_type} =    Get Value    form_select
    Should Be Equal    ${current_reference_type}    ${reference_type}

Set DOI
    [Arguments]    ${doi}
    ${doi-form} =    Get WebElement    xpath://form[@id='doi-form']
    ${doi-input} =    Get WebElement    xpath://form[@id='doi-form']//input[@name='doi_fill']

    Wait Until Element Is Enabled    ${doi-input}
    Wait Until Element Is Visible    ${doi-input}
    Input Text    ${doi-input}    ${doi}

    Submit Form    ${doi-form}

Set Field
    [Arguments]    ${reference_type}    ${field_name}    ${value}
    ${input} =    Get WebElement    xpath://div[@id='${reference_type}']//input[@name='${field_name}']
    Wait Until Element Is Enabled    ${input}
    Wait Until Element Is Visible    ${input}
    Input Text    ${input}    ${value}

Submit Reference
    [Arguments]    ${reference_type}
    Click Button    xpath://div[@id='${reference_type}']//button[@type='submit']
