# Core Capabilities (CRUD)

## Get document content by ID and version number

The **"Get document version content by ID"** endpoint returns the original content file of the document (object) that matches the objectId parameter.

To retrieve the content of a specific version of a document (object), simply add /versions/{versionNr} before /contents/file of the original content GET call, where {versionNr} specifies which version to retrieve.


[Read about Retrieving Documents with the yuuvis® API](https://yuuvis.io/how-to/retrieve)

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/versions/{versionNr}/contents/file

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
