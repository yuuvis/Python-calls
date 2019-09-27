# Core Capabilities (CRUD)

## Validate content digest by ID

For already imported documents, using the [Store one or more documents](https://yuuvis.io/docs/services/yuuvis-api/operations/ObjectsPost?) endpoint, a content digest is automatically generated and stored [(Secure Hash Algorythm, SHA256)](https://tools.ietf.org/html/rfc6234)

To validate the content digest for a stored document, you use the **"Validate content digest by ID"** endpoint. Send a request with the objectId which generates a new content digest based on the currently stored document. This newly generated content digest is compared with the formerly generated and stored one.


## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/actions/validate/digest

## Request headers

| Header                    | Type   | Meaning                                                                                             |
|---------------------------|--------|-----------------------------------------------------------------------------------------------------|
| Ocp-Apim-Subscription-Key | String | Subscription key which provides access to the API. Found on the Subscriptions page of your account. |

## Request body

## Responses

## 200 OK

### OK - The value of the content digest stored in the index data is still correct.

## 404 Not Found

### Not Found - The document (object) with this objectId can not be found.

## 409 Conflict

### Conflict - The generated content digest does not match the value stored in the index data.

### Code example

[Get Validate Content by ID](./Get-Object-Content-Digest.py)
