*** Settings ***
Documentation       Integraatio- ja hyväksymistestaus lähdeviitteiden poistamiselle

Resource            ../../resources/common.robot
Resource            ../../resources/delete.robot
Resource            ../../resources/view.robot

Suite Setup         Run Keywords
...                     Open And Configure Browser    AND
...                     Initialize Database    AND
...                     Reference Count In Database Should Be    0    AND
...                     Add two test articles to database    AND
...                     Reference Count In Database Should Be    2
Suite Teardown      Run Keywords
...                     Close Browser    AND
...                     Initialize Database


*** Test Cases ***
User should be able to delete a reference
    [Documentation]    Käyttäjänä voin poistaa lisättyjä lähdeviitteitä #5

    Go To Search Page

    Click Delete Reference    Peten artikkeli    Petteri Orpo    2001
    Handle Alert

    Reference Deletion Should Be Confirmed
    Search Page Reference Count Should Be    1
    Reference Count In Database Should Be    1


*** Keywords ***
Add two test articles to database
    Add Article To Database    Maijan artikkeli    Maija    2011    Maijan lehti
    Add Article To Database    Peten artikkeli    Petteri Orpo    2001    Peten lehti
