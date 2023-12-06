*** Settings ***
Documentation       Integraatio- ja hyväksymistestaus lähdeviitteiden lisäykselle

Resource            ../../resources/add.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Run Keywords
...                     Initialize Database    AND
...                     Reference Count In Database Should Be    0
Test Teardown       Initialize Database


*** Test Cases ***
User Should Be Able to Add An Article
    [Documentation]    Käyttäjänä pystyn lisäämään "article"-tyyppisen lähdeviitteen,
    ...    joka sisältää kentät (title, author, journal, year, volume, number, page) #1
    Go To Add Page
    Select Reference Type    article
    Set Field    article    author    Pekka Mikkola
    Set Field    article    title    Maijan artikkeli
    Set Field    article    journal    Maijan artikkelikokoelma
    Set Field    article    year    2011
    Submit Reference    article
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Be Able to Add A Book
    [Documentation]    Käyttäjänä pystyn lisäämään "book"-tyyppisen lähdeviitteen #37
    Go To Add Page
    Select Reference Type    book
    Set Field    book    author    Maija Makkonen
    Set Field    book    title    Maijan kirja
    Set Field    book    year    2000
    Set Field    book    publisher    WSOY
    Submit Reference    book
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Be Able to Add An Inproceedings
    [Documentation]    Käyttäjänä pystyn lisäämään "inproceeding"-tyyppisen lähdeviitteen #38
    Go To Add Page
    Select Reference Type    inproceedings
    Set Field    inproceedings    author    Maija
    Set Field    inproceedings    title    Maijan inproceedings
    Set Field    inproceedings    booktitle    Maijan kokoelma
    Set Field    inproceedings    year    2011
    Submit Reference    inproceedings
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Not Be Able to Add An Article Without Required Fields
    [Documentation]    Ei user storya
    Go To Add Page
    Select Reference Type    article
    Set Field    article    author    Pekka Mikkola
    Set Field    article    title    Maijan artikkeli
    Set Field    article    journal    Maijan artikkelikokoelma
    Submit Reference    article
    Reference Addition Should Be Rejected With Invalid Field    article    year
    Reference Count In Database Should Be    0
