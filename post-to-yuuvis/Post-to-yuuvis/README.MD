# Core Capabilities (CRUD)

### API change history

[Documentation](https://yuuvis.io/how-to)


## Store one or more documents

The **"Store one or more documents"** endpoint requires a multipart body with an index data parameter as well as a binary content parameter.

Save your index data as file (e.g. metadata.json) and use it for the data parameter. For the binary content, the cid_63apple parameter, you can use any file you'd like to store. Note that the "Try it" button is not available for this endpoint. You have to try it out externally. Use the provided code samples as a starting point.

If the request is successful, the index data of the previously stored document will be returned in JSON format.

Index Data Example, JSON Format

```
{`
 ` ` ` ` `"objects": [{`
 ` ` ` ` ` ` ` ` `"properties": {`
 ` ` ` ` ` ` ` ` ` ` ` ` `"enaio:objectTypeId": {`
 ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `"value": "document"`
 ` ` ` ` ` ` ` ` ` ` ` ` `},`
 ` ` ` ` ` ` ` ` ` ` ` ` `"Name": {`
 ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `"value": "my document"`
 ` ` ` ` ` ` ` ` ` ` ` ` `}`
 ` ` ` ` ` ` ` ` `},`
 ` ` ` ` ` ` ` ` `"contentStreams": [{`
 ` ` ` ` ` ` ` ` ` ` ` ` `"cid": "cid_63apple"`
 ` ` ` ` ` ` ` ` `}]`
 ` ` ` ` `}]`
 `}
 ```
[Read about Storing Documents with the yuuvis® API](https://yuuvis.io/how-to/import)

## Request

### Request URL

https://api.yuuvis.io/dms/objects


## Request parameters

```
    -data (optional)                File
    ------------------------------------
    -cid_63apple (optional)         File
```
## Request headers

Content-Type (optional) string Media type of the body sent to the API.
Ocp-Apim-Subscription-Key string Subscription key which provides access to this API. Found in your Profile.

## Request body

```
-**data** *required
string ($binary) 
index data for the document (object) to be imported as JSON file

-**cid_63apple** *required
string ($binary) 
document (object) itself to be imported as binary file
```


Note: Make sure the `cid_63apple` ID is referenced in the corresponding index data

multipart/form-data

## Responses

## 200 OK                         

### OK                           



## Representations


### sample
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
  ]
}
```
### Schema

```
{
  "title": "Import Object Response",
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
    ]
  }
}
```
## 401 Unauthorized

###   Unauthorized

### Code example

[Mulitpart-body post request](./Post-to-yuuvis.py)
