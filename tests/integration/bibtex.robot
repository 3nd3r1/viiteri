*** Settings ***
Resource            ../../resources/common.robot
Resource            ../../resources/bibtex.robot

Suite Setup         Run Keywords
...                     Open And Configure Browser    AND
...                     Initialize Database    AND
...                     Reference Count In Database Should Be    0
Suite Teardown      Run Keywords
...                     Close Browser    AND
...                     Initialize Database


*** Test Cases ***
User Should Be Able To See All Added References In Bibtex Format
    [Documentation]

    Add Article To Database    Maijan artikkeli    Maija    2011    Maijan lehti
    Go To Bibtex Page
    Page Should Contain Reference    @article    author = "Maija"    title = "Maijan artikkeli"    journal = "Maijan lehti"    year = "2011"
