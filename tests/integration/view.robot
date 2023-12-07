*** Settings ***
Documentation       Integraatio- ja hyväksymistestaus lähdeviitteiden näkemiseen

Resource            ../../resources/common.robot
Resource            ../../resources/view.robot
Library             Dialogs

Suite Setup         Run Keywords
...                     Open And Configure Browser    AND
...                     Initialize Database    AND
...                     Add two test articles to database    AND
...                     Clear Clipboard
Suite Teardown      Run Keywords
...                     Close Browser    AND
...                     Initialize Database    AND
...                     Clear Clipboard


*** Test Cases ***
User should be able to see all added references in table format
    [Documentation]    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet siistissä muodossa #36
    ...    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet. #2
    ...    Käyttäjänä pystyn näkemään lisäämäni lähdeviitteet taulukkomaisessa muodossa #63

    Go To View Table Page

    View Table Page Should Contain Reference    Maijan artikkeli    Maija    2011
    View Table Page Should Contain Reference    Peten artikkeli    Petteri Orpo    2001

    View Table Page Reference Count Should Be    2

User should be able to see all added references in bibtex format
    [Documentation]    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet bibtex-muodossa. #60

    Go To View Bibtex Page

    View Bibtex Page Should Contain Reference    article    Maijan artikkeli    Maija    2011
    View Bibtex Page Should Contain Reference    article    Peten artikkeli    Petteri Orpo    2001

# User should be able to copy all references in bibtex format to the clipboard
#    [Documentation]    Käyttäjänä pystyn napin painalluksella kopioimaan bibtex-muotoiset lähdeviitteet leikepöydälle #62
#
#    Go To View Bibtex Page
#
#    Click Copy All To Clipboard Button
#
#    Clipboard Should Contain Reference    article    Maijan artikkeli    Maija    2011
#    Clipboard Should Contain Reference    article    Peten artikkeli    Petteri Orpo    2001


*** Keywords ***
Add two test articles to database
    Add Article To Database    Maijan artikkeli    Maija    2011    Maijan lehti
    Add Article To Database    Peten artikkeli    Petteri Orpo    2001    Peten lehti

    Reference Count In Database Should Be    2
