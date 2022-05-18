# API

## User Registration
### Endpoint : http://127.0.0.1:8000/api/register/
### Format : {
     username: alex
     email: alex@example.com
     password: dummy1
### }
### Response : {
     email: alex@example.com
     username: alex
### }

## Token Generation
### Endpoint : http://127.0.0.1:8000/api-token-auth/ 
### Format : {
     username: alex
     password: dummy1
### }
### Response : {
    token: 493ec97b247ba51892098a43af70bf5126f9a723
### }
 
## Message
### Endpoint : http://127.0.0.1:8000/api/message/
### Format for new message: {
     text: this is message text
     token: 493ec97b247ba51892098a43af70bf5126f9a723
### }
### Response : {
    "data": {
        "created_at": "2022-05-18T17:19:11.957264Z",
        "created_by": 101,
        "id": 1,
        "text": "this is message text",
        "updated_at": "2022-05-18T17:19:11.957264Z"
    },
    "status": "success"
### }
### Format for existing message: {
    id:1
    text: this is message text
    token: 493ec97b247ba51892098a43af70bf5126f9a723
### }
