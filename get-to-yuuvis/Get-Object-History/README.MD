# Core Capabilities (CRUD)

### API change history

[Documentation](https://yuuvis.io/how-to)



## Get a list of history entries by ID

The **"Get a list of history entries by ID"** endpoint retrieves information about the actions and modifications that have been carried out for the given document (object) - objectId parameter. Each action or modification is stored in a separate history entry.

[Read about Retrieving the History Entries of a Document with the yuuvis® API](https://yuuvis.io/how-to/retrieve_hist)


## Meaning of field values

### ValueDetail	                        Meaning
```
100	CREATE_METADATA	                Document without document file was created
101	CREATE_METADATA_WITH_CONTENT	Document including document file was created
201	DELETE_CONTENT	                Document file was deleted
300	UPDATE_METADATA	                Metadata has been updated
301	UPDATE_CONTENT	                Document file has been updated
302	UPDATE_METADATA_WITH_CONTENT	Index data and document file has been updated
400	GET_CONTENT	                    Document file was downloaded
401	GET_METADATA	                Index data was retrieved
402	GET_TEXT_RENDITION	            Text preview was downloaded
403	GET_PDF_RENDITION	            Document file was downloaded as PDF
404	GET_THUMBNAIL_RENDITION	        Thumbnail preview has been downloaded

```
[Try It](https://yuuvis.io/docs/services/yuuvis-dms-core/operations/ObjectsHistoryByObjectIdGet/console)

## Request

### Request URL

https://api.yuuvis.io/dms/objects/{objectId}/history

## Request parameters

```

objectId            string          The objectID of the document (object) for which the history entries are to be retrieved.

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

`application/json`

### Sample
```

 {
  "objects": [
    {
      "properties": {
        "enaio:objectId": {
          "value": 435902492049473540
        },
        "enaio:objectTypeId": {
          "value": "enaio:audit"
        },
        "enaio:baseTypeId": {
          "value": "item"
        },
        "enaio:createdBy": {
          "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
        },
        "enaio:tenant": {
          "value": "heckathon"
        },
        "enaio:creationDate": {
          "value": ""
        },
        "description": {
          "value": ""
        },
        "action": {
          "value": 101
        },
        "detail": {
          "value": "CREATE_METADATA_WITH_CONTENT"
        },
        "referredObjectId": {
          "value": "7c097bde-8c63-4764-a85d-0205a17eb2f2"
        },
        "enaio:traceId": {
          "value": "49749ababad604f3"
        },
        "enaio:versionNumber": {
          "value": 1
        }
      }
    },
    {
      "properties": {
        "enaio:objectId": {
          "value": 435902492049473540
        },
        "enaio:objectTypeId": {
          "value": "enaio:audit"
        },
        "enaio:baseTypeId": {
          "value": "item"
        },
        "enaio:createdBy": {
          "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
        },
        "enaio:tenant": {
          "value": "heckathon"
        },
        "enaio:creationDate": {
          "value": ""
        },
        "description": {
          "value": ""
        },
        "action": {
          "value": 401
        },
        "detail": {
          "value": "GET_METADATA"
        },
        "referredObjectId": {
          "value": "7c097bde-8c63-4764-a85d-0205a17eb2f2"
        },
        "enaio:traceId": {
          "value": "49749ababad604f3"
        },
        "enaio:versionNumber": {
          "value": 1
        }
      }
    },
    {
      "properties": {
        "enaio:objectId": {
          "value": 435902492049473540
        },
        "enaio:objectTypeId": {
          "value": "enaio:audit"
        },
        "enaio:baseTypeId": {
          "value": "item"
        },
        "enaio:createdBy": {
          "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
        },
        "enaio:tenant": {
          "value": "hackathon"
        },
        "enaio:creationDate": {
          "value": ""
        },
        "description": {
          "value": ""
        },
        "action": {
          "value": 301
        },
        "detail": {
          "value": "UPDATE_CONTENT"
        },
        "referredObjectId": {
          "value": "7c097bde-8c63-4764-a85d-0205a17eb2f2"
        },
        "enaio:traceId": {
          "value": "49749ababad604f3"
        },
        "enaio:versionNumber": {
          "value": 2
        }
      }
    }
  ]
}

```

### Schema
```
{
  "title": "History Entries List",
  "required": [
    "objects"
  ],
  "type": "object",
  "properties": {
    "objects": {
      "type": "array",
      "items": {
        "title": "History Entry Object",
        "type": "object",
        "properties": {
          "properties": {
            "required": [
              "action",
              "description",
              "detail",
              "enaio:baseTypeId",
              "enaio:createdBy",
              "enaio:creationDate",
              "enaio:objectId",
              "enaio:objectTypeId",
              "enaio:tenant",
              "enaio:traceId",
              "enaio:versionNumber",
              "referredObjectId"
            ],
            "type": "object",
            "properties": {
              "enaio:objectId": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "integer",
                    "format": "int64"
                  }
                }
              },
              "enaio:objectTypeId": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "enaio:baseTypeId": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "enaio:createdBy": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "enaio:tenant": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "enaio:creationDate": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "description": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "action": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "integer",
                    "format": "int32"
                  }
                }
              },
              "detail": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "referredObjectId": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "enaio:traceId": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "string"
                  }
                }
              },
              "enaio:versionNumber": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "integer",
                    "format": "int32"
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
          "enaio:objectId": {
            "value": 435902492049473540
          },
          "enaio:objectTypeId": {
            "value": "enaio:audit"
          },
          "enaio:baseTypeId": {
            "value": "item"
          },
          "enaio:createdBy": {
            "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
          },
          "enaio:tenant": {
            "value": "heckathon"
          },
          "enaio:creationDate": {
            "value": ""
          },
          "description": {
            "value": ""
          },
          "action": {
            "value": 101
          },
          "detail": {
            "value": "CREATE_METADATA_WITH_CONTENT"
          },
          "referredObjectId": {
            "value": "7c097bde-8c63-4764-a85d-0205a17eb2f2"
          },
          "enaio:traceId": {
            "value": "49749ababad604f3"
          },
          "enaio:versionNumber": {
            "value": 1
          }
        }
      },
      {
        "properties": {
          "enaio:objectId": {
            "value": 435902492049473540
          },
          "enaio:objectTypeId": {
            "value": "enaio:audit"
          },
          "enaio:baseTypeId": {
            "value": "item"
          },
          "enaio:createdBy": {
            "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
          },
          "enaio:tenant": {
            "value": "heckathon"
          },
          "enaio:creationDate": {
            "value": ""
          },
          "description": {
            "value": ""
          },
          "action": {
            "value": 401
          },
          "detail": {
            "value": "GET_METADATA"
          },
          "referredObjectId": {
            "value": "7c097bde-8c63-4764-a85d-0205a17eb2f2"
          },
          "enaio:traceId": {
            "value": "49749ababad604f3"
          },
          "enaio:versionNumber": {
            "value": 1
          }
        }
      },
      {
        "properties": {
          "enaio:objectId": {
            "value": 435902492049473540
          },
          "enaio:objectTypeId": {
            "value": "enaio:audit"
          },
          "enaio:baseTypeId": {
            "value": "item"
          },
          "enaio:createdBy": {
            "value": "ac3fbec5-b99d-4323-9235-cf6e4c6a2be7"
          },
          "enaio:tenant": {
            "value": "hackathon"
          },
          "enaio:creationDate": {
            "value": ""
          },
          "description": {
            "value": ""
          },
          "action": {
            "value": 301
          },
          "detail": {
            "value": "UPDATE_CONTENT"
          },
          "referredObjectId": {
            "value": "7c097bde-8c63-4764-a85d-0205a17eb2f2"
          },
          "enaio:traceId": {
            "value": "49749ababad604f3"
          },
          "enaio:versionNumber": {
            "value": 2
          }
        }
      }
    ]
  }
}
```


## 404 Not Found

### Not Found

### Code samples

[Get-Object-History.py](./Get-Object-History.py)