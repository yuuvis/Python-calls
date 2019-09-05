# Core Capabilities (CRUD)

## Update document content by ID

The **"Update document content by ID"** endpoint updates the content file of the document (object) that matches the objectId parameter. You can name the content by passing the file name over to the Content-Disposition header.


[Read about Updating Documents with the yuuvis® API](https://yuuvis.io/how-to/update)

### Request URL

https://api.yuuvis.io/dms/objects/{objectId}/contents/file


## Request headers

```
Content-Disposition                 string      format: attachment;filename=myfilename

--------------------------------------------------------------------------------------------------------------------------------

Content-Type (optional)             string      Media type of the body sent to the API.

--------------------------------------------------------------------------------------------------------------------------------

Ocp-Apim-Subscription-Key           string      Subscription key which provides access to this API. Found in your Profile.

```

## Request body

`application/octet-stream`

## Responses        

## 200 OK        

### OK

## Representations

`application/json`

### Sample
```

 {
  "objects": [
    {
      "properties": {
        "enaio:objectId": {
          "value": "c5ef052e-4869-487a-8599-58ecaa093583"
        },
        "enaio:baseTypeId": {
          "value": "enaio:document"
        },
        "enaio:objectTypeId": {
          "value": "document"
        },
        "enaio:createdBy": {
          "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
        },
        "enaio:creationDate": {
          "value": "2019-03-20T13:34:20.15Z"
        },
        "enaio:lastModifiedBy": {
          "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
        },
        "enaio:lastModificationDate": {
          "value": "2019-03-20T13:34:20.15Z"
        },
        "enaio:versionNumber": {
          "value": 2
        },
        "enaio:tenant": {
          "value": "heckathon"
        },
        "enaio:traceId": {
          "value": "49749ababad604f3"
        },
        "Name": {
          "value": "Update Email"
        }
      },
      "contentStreams": [
        {
          "contentStreamId": "DD8A546A-4B14-11E9-B059-79C8490F4220",
          "archivePath": "heckathon/2019/03/20/",
          "length": 431397,
          "mimeType": "message/rfc822",
          "fileName": "import.eml",
          "digest": "11857B6FAD61E41AFB3E7398BA1BA4BFB6B0A5422762FF41A0907BC0BFF7748F",
          "repositoryId": "s3miniowithpath"
        }
      ]
    }
  ]
}
```
### Scheam

```
{
  "title": "Update Metadata Response",
  "required": [
    "objects"
  ],
  "type": "object",
  "properties": {
    "objects": {
      "type": "array",
      "items": {
        "title": "Metadata Object",
        "required": [
          "properties"
        ],
        "type": "object",
        "properties": {
          "properties": {
            "required": [
              "enaio:objectTypeId"
            ],
            "type": "object",
            "properties": {
              "enaio:objectTypeId": {
                "required": [
                  "value"
                ],
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "Name": {
                "required": [
                  "value"
                ],
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      }
    },
    "contentStreams": {
      "type": "array",
      "items": {
        "title": "Content Stream Object",
        "required": [
          "archivePath",
          "contentStreamId",
          "digest",
          "fileName",
          "length",
          "mimeType",
          "repositoryId"
        ],
        "type": "object",
        "properties": {
          "contentStreamId": {
            "type": "string"
          },
          "archivePath": {
            "type": "string"
          },
          "length": {
            "type": "integer",
            "format": "int64"
          },
          "mimeType": {
            "type": "string"
          },
          "fileName": {
            "type": "string"
          },
          "digest": {
            "type": "string"
          },
          "repositoryId": {
            "type": "string"
          }
        }
      }
    }
  },
  "example": {
    "objects": [
      {
        "properties": {
          "enaio:objectId": {
            "value": "c5ef052e-4869-487a-8599-58ecaa093583"
          },
          "enaio:baseTypeId": {
            "value": "enaio:document"
          },
          "enaio:objectTypeId": {
            "value": "document"
          },
          "enaio:createdBy": {
            "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
          },
          "enaio:creationDate": {
            "value": "2019-03-20T13:34:20.15Z"
          },
          "enaio:lastModifiedBy": {
            "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
          },
          "enaio:lastModificationDate": {
            "value": "2019-03-20T13:34:20.15Z"
          },
          "enaio:versionNumber": {
            "value": 2
          },
          "enaio:tenant": {
            "value": "heckathon"
          },
          "enaio:traceId": {
            "value": "49749ababad604f3"
          },
          "Name": {
            "value": "Update Email"
          }
        },
        "contentStreams": [
          {
            "contentStreamId": "DD8A546A-4B14-11E9-B059-79C8490F4220",
            "archivePath": "heckathon/2019/03/20/",
            "length": 431397,
            "mimeType": "message/rfc822",
            "fileName": "import.eml",
            "digest": "11857B6FAD61E41AFB3E7398BA1BA4BFB6B0A5422762FF41A0907BC0BFF7748F",
            "repositoryId": "s3miniowithpath"
          }
        ]
      }
    ]
  }
}
```

## 404 Not Found

### NOT FOUND



### Code examples

[Update document content by ID](./Post-Object-Update-Content.html)
