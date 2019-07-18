# Core Capabilities (CRUD)

### API change history

[Documentation](https://yuuvis.io/how-to)


## Get an image rendition

The **"Get an image rendition"** endpoint generates and returns a PNG file of the content's first page of the document (object) that matches the objectId parameter. This PNG file is a small preview with the maximum dimensions 256x256.

[Try It](https://yuuvis.io/docs/services/yuuvis-dms-core/operations/get-dms-objects-objectid-contents-renditions-slide/console)

## Request

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/renditions/slide

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