# yuuvis® Ultimate

### API change history

[Documentation](https://yuuvis.portal.azure-api.net/how-to)

**yuuvis® Ultimate** is the ultimate freedom to innovate. Get access to the latest API endpoints as the yuuvis® development team releases them on its journey to aPaas.

## Get an image rendition

The **"Get an image rendition"** endpoint generates and returns a PNG file of the content's first page of the document (object) that matches the objectId parameter. This PNG file is a small preview with the maximum dimensions 256x256.

## Request

## Request URL

https://yuuvis.azure-api.net/dms/objects/{objectId}/contents/renditions/slide

## Request parameters

```
objectId            string          The objectId of the document (object) to be requested.

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

`image/png`

## 404 Not Found

### NOT FOUND

### Code example
[Get a image Rendition](./Get-a-image-Rendition-to-yuuvis.py)