# Core Capabilities (CRUD)

## Get a text rendition

The **"Get a text rendition"** endpoint generates and returns a text rendition of the content of the document (object) that matches the objectId parameter.


[Read about Retrieving Document Renditions with the yuuvis® API](https://yuuvis.io/how-to/rendition)

### Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/renditions/text

## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

## Responses

## 200 OK

### OK

## Representations

`text/plain`

## 404 Not Found

### NOT FOUND

### Code samples

[Get a text rendition](./Get-Rendition-Text.py)
