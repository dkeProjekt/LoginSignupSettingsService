# Login Service

### SET-UP

#### 1) Aufruf in der Konsole:

`docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4`

### REST-CALL

#### 1) User Einloggen

`localhost:5001/login`

###### Request:

`{
"username" : "Liam",
"password": "pwd12345"
}`

###### Response:

`{
    "login_successful" : "True",
    "username": "Liam",
    "error": ""
}`
