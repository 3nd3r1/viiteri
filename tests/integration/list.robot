*** Settings ***
Resource            ../../resources/common.robot
Resource            ../../resources/list.robot

Suite Setup         Run Keywords
...                     Open And Configure Browser    AND
...                     Initialize Database    AND
...                     Reference Count In Database Should Be    0
Suite Teardown      Run Keywords
...                     Close Browser    AND
...                     Initialize Database


*** Test Cases ***
User should be able to see all added references
    [Documentation]    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet siistissä muodossa #36
    ...    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet. #2
    ...    Käyttäjänä pystyn näkemään lisäämäni lähdeviitteet taulukkomaisessa muodossa #63

    Add Article To Database    Maijan artikkeli    Pekka Mikkola    2011    Maijan lehti
    Add Article To Database    Peten artikkeli    Petteri Orpo    2001    Peten lehti

    Go To List Page

    Page Should Contain Reference    Maijan artikkeli    Pekka Mikkola    2011
    Page Should Contain Reference    Peten artikkeli    Petteri Orpo    2001

    Page Reference Count Should Be    2


User Should Be Able To Delete A Reference
    [Documentation]    Käyttäjänä voin poistaa lisättyjä lähdeviitteitä #5

    View Whole Reference
    Page Should Contain Whole Reference    Maijan lehti
    ${button} =    Get WebElement    xpath://tbody/tr[@class='button-row']/td/button[@class='delete-button']
    Click Element    ${button}
    Handle Alert
    Page Reference Count Should Be    1