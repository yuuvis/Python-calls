# Core Capabilities (CRUD)

### API change history

[Documentation](https://api.yuuvis.io/how-to)


## Get a text rendition

The **"Get a text rendition"** endpoint generates and returns a text rendition of the content of the document (object) that matches the objectId parameter.

[Try It](https://yuuvis.io/docs/services/yuuvis-dms-core/operations/get-dms-objects-objectid-contents-renditions-text/console)

## Request

### Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/renditions/text

## Request parameters

```
objectId            string              The objectId of the document (object) to be requested.
```

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

[Get a text rendition](./Get-a-text-Rendition.py)