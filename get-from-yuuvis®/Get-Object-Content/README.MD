# Core Capabilities (CRUD)

## Get document content by ID

The **"Get document content by ID"** endpoint returns the original content file of the document (object) that matches the objectId parameter.


[Read about Retrieving Documents with the yuuvis® API](https://yuuvis.io/how-to/retrieve)

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/file

## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```
## Request body

## Responses

## 200 OK

### OK

## 404 Not Found

### NOT FOUND

### Code samples

[Get document content by ID](./Get-Object-Content.py)
