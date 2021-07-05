# Settings Service

### SET-UP

#### 1) Aufruf in der Konsole:

`docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4`

### REST-CALL

#### 1) Persönliche Daten Abrufen
`localhost:5003/get_personal_data`

###### Request:

`{
    "username" : "Liam"
}`

###### Response:

`{
    "get_data_successful" : "True",
    "username": "Liam",
    "email": "fake@mail.com"
    "registration_date": "2021-07-05"
    "error": ""
}`



#### 2) Passwort Ändern

`localhost:5003/change_password`

###### Request:

`{
    "username" : "Liam",
    "password_old": "pwd12345",
    "password_new": "asdf"
}`

###### Response:

`{
    "change_password_successful" : "True",
    "username": "Liam",
    "error": ""
}`
