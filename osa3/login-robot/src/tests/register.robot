*** Settings ***
Resource  resource.robot
Library  ../AppLibrary.py
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Create User  pekka  Salasana123!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  UusiSalis123!
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Create User  ka  Salasana123!
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Create User  k4lle  Salasana123!
    Output Should Contain  Username must contain only lowercase letters a-z

Register With Valid Username And Too Short Password
    Create User  erkki  sala1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  jorma  Salasanaaaaa
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123