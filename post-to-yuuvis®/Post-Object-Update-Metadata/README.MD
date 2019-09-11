# Core Capabilities (CRUD)

## Update document index data by ID

The **"Update document index data by ID"** endpoint updates the index data of the document (object) that matches the objectId parameter.

To update the index data send the request with the new index data as request body and the ID of the document (object) as objectId. If one of the properties is missing in the new index data, it will be removed from the document (object).
Most of the system properties cannot be updated or are updated automatically. If the new index data contains these properties, their values must match the values of the current version. Hence you can retrieve the current index data using the [GET document index data by ID](https://yuuvis.io/docs/services/yuuvis-api/operations/ObjectsByObjectIdGet?) endpoint first, to use the result. Edit some properties and post it again using this endpoint.
Note that the "Try it" button is not available for this endpoint. You have to try it out externally. Use the provided code samples as a starting point.

[Read about Updating Documents with the yuuvis® API](https://yuuvis.io/how-to/update)

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}

## Request headers

```
Content-Type (optional)             string          Media type of the body sent to the API.

-----------------------------------------------------------------------------------------------------------------------------------

Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```


## Request body

The updated index data is passed as JSON structure in the body as follows.
Note that no ContentStreams object is present within the new metadata, as no simultaneous content update can be made. 

`application/json`

### Sample
```
{
  "objects": [
    {
      "properties": {
        "enaio:objectTypeId": {
          "value": "document"
        },
        "Name": {
          "value": "Update Email"
        }
      }
    }
  ]
}

```
### Schema
```
{
  "title": "Update Metadata Request",
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
    }
  },
  "example": {
    "objects": [
      {
        "properties": {
          "enaio:objectTypeId": {
            "value": "document"
          },
          "Name": {
            "value": "Update Email"
          }
        }
      }
    ]
  }
}
```

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
### Schema

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

##  404 Not Found

### Not Found

### Code samples

[Update document index data by ID](./Post-Object-Update-Metadata.html)
