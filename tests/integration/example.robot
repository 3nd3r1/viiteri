*** Settings ***
Resource            ../../resources/common.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser


*** Test Cases ***
Click Home Link
    Go To Home Page
    Home Page Should Be Open
