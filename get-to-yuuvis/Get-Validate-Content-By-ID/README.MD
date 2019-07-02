# yuuvis® Ultimate

### API change history

[Documentation](https://yuuvis.portal.azure-api.net/how-to)

**yuuvis® Ultimate** is the ultimate freedom to innovate. Get access to the latest API endpoints as the yuuvis® development team releases them on its journey to aPaas.

## Validate content digest by ID

For already imported documents, using the Store one or more documents endpoint, a content digest is automatically generated and stored [(Secure Hash Algorythm, SHA256)](https://tools.ietf.org/html/rfc6234)

To validate the content digest for a stored document, you use the **"Validate content digest by ID"** endpoint. Send a request with the objectId which generates a new content digest based on the currently stored document. This newly generated content digest is compared with the formerly generated and stored one.

## Request

## Request URL

https://yuuvis.azure-api.net/dms/objects/{objectId}/actions/validate/digest

## Request parameters

```
objectId            string          The objectId of the document (object) for which the content digest is to be validated.

```

## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

## Responses

## 200 OK

### OK - The value of the content digest stored in the index data is still correct.

## 404 Not Found

### Not Found - The document (object) with this objectId can not be found.

## 409 Conflict

### Conflict - The generated content digest does not match the value stored in the index data.

### Code example

[Get Validate Content by ID](./Get-Validate-Content-by-ID-to-yuuvis.py)