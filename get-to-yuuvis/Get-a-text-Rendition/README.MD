# yuuvis® Ultimate

### API change history

[Documentation](https://yuuvis.portal.azure-api.net/how-to)

**yuuvis® Ultimate** is the ultimate freedom to innovate. Get access to the latest API endpoints as the yuuvis® development team releases them on its journey to aPaas.

## Get a text rendition

The **"Get a text rendition"** endpoint generates and returns a text rendition of the content of the document (object) that matches the objectId parameter.

## Request

### Request URL

https://yuuvis.azure-api.net/dms/objects/{objectId}/contents/renditions/text

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