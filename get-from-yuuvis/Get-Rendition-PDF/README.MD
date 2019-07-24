# Core Capabilities (CRUD)

### API change history

[Documentation](https://yuuvis.io/how-to)


## Get a PDF rendition

The **"Get a PDF rendition"** endpoint generates and returns a PDF rendition of the content of the document (object) that matches the objectId parameter. Note that the PDF file cannot be displayed using the Azure portal. Please use another tool, such as Postman, to download the PDF rendition file.

[Try It](https://yuuvis.io/docs/services/yuuvis-dms-core/operations/get-dms-objects-objectid-contents-renditions-pdf/console)
## Request

### Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/renditions/pdf

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

`application/pdf`

## 404 Not Found

### NOT FOUND


### Code example

[Get a PDF Rendition](./Get-Rendition-PDF.py)