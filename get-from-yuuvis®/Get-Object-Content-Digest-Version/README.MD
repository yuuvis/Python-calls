# Core Capabilities (CRUD)

## Validate content digest by ID and version number

For already imported documents, using the [Store one or more documents](https://yuuvis.io/docs/services/yuuvis-api/operations/ObjectsPost?) endpoint, a content digest is automatically generated and stored [(Secure Hash Algorythm, SHA256)](https://tools.ietf.org/html/rfc6234)

To validate the content digest for a stored document, you use the **"Validate content digest by ID"** endpoint. Send a request with the objectId which generates a new content digest based on the currently stored document. This newly generated content digest is compared with the formerly generated and stored one.

To validate the content digest of a specific document (object) version, simply add a /versions/{versionNr} between the objectId and the suffix beginning with /actions.


## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/versions/{versionNr}/actions/validate/digest

## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

## Responses

## 200 OK

### OK - The value of the content digest of the specified version stored in the index data is still correct.

## 404 Not Found

### Not Found - The document (object) with this objectId and this version number can not be found.

## 409 Conflict

### Conflict - The generated content digest of the specified version does not match the value stored in the index data.

### Code example

[Get Validate Content by ID](./Get-Object-Content-Digest-Version.py)
