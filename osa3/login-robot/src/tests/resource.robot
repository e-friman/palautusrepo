*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input New Command
    Input  new

Create User
    [Arguments]  ${username}  ${password}
    Input new Command
    Input  ${username}
    Input  ${password}
    Run Application


Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
