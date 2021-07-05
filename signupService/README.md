# Sign Up Service

### SET-UP

#### 1) Aufruf in der Konsole:

`docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4`

### REST-CALL

#### 1) Sign Up
`localhost:5002/signup`

###### Request:

`{
    "email": "fake@mail.com",
    "username" : "Liam",
    "password": "pwd12345"
}`

###### Response:

`{
    "signup_successful" : "True",
    "username": "Liam",
    "error": ""
}`



#### 2) Liste Aller Registrierten User Laden

`localhost:5002/get_all_users`

###### Request:

`{
}`

###### Response:

`{
    "get_all_users_successful" : "True",
    "list_of_users": ["Elton", "Anna", "Tony"]
}`
