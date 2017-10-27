# Messages endpoint
Simple API to GET, POST, PATCH, and DELETE `Message` entities. I've deployed it on heroku and an endpoint has been exposed at 

_http://greystone.duri.im/message_

Request Body as specified :
```
{
    "message_text": "Hey Greystone!!"
}
```
_GET_
```
http://greystone.duri.im/message/
```

_POST_, _PATCH_, or _DELETE_
```
http://greystone.duri.im/message/{id}/
```
