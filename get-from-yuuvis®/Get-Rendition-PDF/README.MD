# Core Capabilities (CRUD)

## Get a PDF rendition

The **"Get a PDF rendition"** endpoint generates and returns a PDF rendition of the content of the document (object) that matches the objectId parameter. Note that the PDF file cannot be displayed using the Azure portal. Please use another tool, such as Postman, to download the PDF rendition file.


[Read about Retrieving Document Renditions with the yuuvis® API](https://yuuvis.io/how-to/rendition)

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/renditions/pdf

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
