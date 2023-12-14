*** Settings ***
Documentation       Integraatio- ja hyväksymistestaus lähdeviitteiden näkemiseen

Resource            ../../resources/common.robot
Resource            ../../resources/view.robot
Library             RPA.Desktop

Suite Setup         Run Keywords
...                     Open And Configure Browser    AND
...                     Initialize Database    AND
...                     Add two test articles to database
Suite Teardown      Run Keywords
...                     Close Browser    AND
...                     Initialize Database


*** Test Cases ***
User should be able to see all added references in table format
    [Documentation]    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet siistissä muodossa #36
    ...    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet. #2
    ...    Käyttäjänä pystyn näkemään lisäämäni lähdeviitteet taulukkomaisessa muodossa #63

    Go To Search Page

    Search Page Should Contain Reference    Maijan artikkeli    Maija    2011
    Search Page Should Contain Reference    Peten artikkeli    Petteri Orpo    2001

    Search Page Reference Count Should Be    2

User Should Be Able To Search For References
    [Documentation]    Käyttäjänä voin rajoittaa lähdeviitteitä avainsanan avulla #4
    Go To Search Page

    Input And Submit Search Term    pete

    Search Page Should Contain Reference    Peten artikkeli    Petteri Orpo    2001

User Should Be Able To Search For References Using Or Operator
    [Documentation]    Käyttäjänä voin rajoittaa lähdeviitteitä avainsanan avulla #4
    Go To Search Page

    Input And Submit Search Term    pete, maija

    Search Page Should Contain Reference    Maijan artikkeli    Maija    2011
    Search Page Should Contain Reference    Peten artikkeli    Petteri Orpo    2001

User Should Be Able To Search For References Using And Operator
    [Documentation]    Käyttäjänä voin rajoittaa lähdeviitteitä avainsanan avulla #4
    Go To Search Page

    Input And Submit Search Term    pete, &orpo

    Search Page Should Contain Reference    Peten artikkeli    Petteri Orpo    2001

User should be able to see all added references in bibtex format
    [Documentation]    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet bibtex-muodossa. #60
    ...    Käyttäjänä pystyn näkemään kaikki lisätyt lähdeviitteet oikein sisennetyssä bibtex muodossa #99

    Go To Raw BibTex Page

    Raw BibTex Page Should Contain Reference    article    Maijan artikkeli    Maija    2011
    Raw BibTex Page Should Contain Reference    article    Peten artikkeli    Petteri Orpo    2001

User should be able to click on a reference to open an expanded view of the reference details, which are presented in a neat format
    [Documentation]    Käyttäjänä pystyn klikkaamaan lähdeviitelistauksesta yksittäistä viitettä
    ...    avatakseni suuremman näkymän viitteen tietoihin, joka on siistissä muodossa #65

    Go To Search Page

    Click Reference    Maijan artikkeli    Maija    2011

    Search Page Should Contain Extended Reference Details With Fields
    ...    Title=Maijan artikkeli
    ...    Author=Maija
    ...    Year=2011
    ...    Journal=Maijan lehti


*** Keywords ***
Add two test articles to database
    Add Article To Database    Maijan artikkeli    Maija    2011    Maijan lehti
    Add Article To Database    Peten artikkeli    Petteri Orpo    2001    Peten lehti

    Reference Count In Database Should Be    2

Input And Submit Search Term
    [Arguments]    ${searchTerm}
    Input Text    name=search    ${searchTerm}
    Click Button    xpath=//button[contains(text(),'Search')]
