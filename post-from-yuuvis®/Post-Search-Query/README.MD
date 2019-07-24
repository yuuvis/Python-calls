# Core Capabilities (CRUD)

### API change history

[Documentation](https://yuuvis.io/how-to)


## Search documents by search query

The **"Search documents by search query"** endpoint requires a JSON body containing your search query.

The search parameters skipCount and maxItems allow paging for search queries, whereby maxItems defines the maximum number of entries in the hit list and skipCount the maximum number of entries to be skipped.

[Learn about the yuuvis® CMIS-Based Query Language](https://yuuvis.io/how-to/CMIS)

## Request

### Request URL

https://api.yuuvis.io/dms/objects/search

## Request headers

```
Content-Type (optional)         string      Media type of the body sent to the API.
----------------------------------------------------------------------------------------------------------------------
Ocp-Apim-Subscription-Key       string      Subscription key which provides access to this API. Found in your Profile.

```
## Request body

A *search query* consists of three parameters:

- **statement** - the SELECT statement (CMIS-Based Query Language)
- **skipCount** - defines the maximum number of entries to be skipped (for paging)
-  **maxItems** - defines the maximum number of entries in the hit list


`application/json`

### Sample

```
{
  "query": {
    "statement": "SELECT * FROM enaio:object",
    "skipCount": 0,
    "maxItems": 50
  }
}
```

### Schema
```
 {
  "title": "Search Request",
  "required": [
    "query"
  ],
  "type": "object",
  "properties": {
    "query": {
      "required": [
        "maxItems",
        "skipCount",
        "statement"
      ],
      "type": "object",
      "properties": {
        "statement": {
          "type": "string"
        },
        "skipCount": {
          "type": "integer",
          "format": "int32"
        },
        "maxItems": {
          "type": "integer",
          "format": "int32"
        }
      }
    }
  },
  "example": {
    "query": {
      "statement": "SELECT * FROM enaio:object",
      "skipCount": 0,
      "maxItems": 50
    }
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
          "value": 1
        },
        "enaio:tenant": {
          "value": "heckathon"
        },
        "enaio:traceId": {
          "value": "49749ababad604f3"
        },
        "Name": {
          "value": "my document"
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
  ],
  "numItems": 1,
  "hasMoreItems": false,
  "totalNumItems": 1
}
```
### Schema

```
{
  "title": "Search Response Object",
  "required": [
    "hasMoreItems",
    "numItems",
    "objects",
    "totalNumItems"
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
    "numItems": {
      "type": "integer",
      "format": "int64"
    },
    "hasMoreItems": {
      "type": "boolean"
    },
    "totalNumItems": {
      "type": "integer",
      "format": "int64"
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
            "value": 1
          },
          "enaio:tenant": {
            "value": "heckathon"
          },
          "enaio:traceId": {
            "value": "49749ababad604f3"
          },
          "Name": {
            "value": "my document"
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
    ],
    "numItems": 1,
    "hasMoreItems": false,
    "totalNumItems": 1
  }
}
```

### Code example

[Search documents by search query](./Post-Search-Query.py)