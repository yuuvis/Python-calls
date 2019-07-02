# yuuvis® Ultimate

### API change history

[Documentation](https://yuuvis.portal.azure-api.net/how-to)

**yuuvis® Ultimate** is the ultimate freedom to innovate. Get access to the latest API endpoints as the yuuvis® development team releases them on its journey to aPaas.

## Get the raw tenant schema

The **"Get the raw tenant schema"** endpoint returns the raw schema of the tenant (XML) belonging to you as the logged on user.

[Learn about yuuvis® API schemas](https://yuuvis.portal.azure-api.net/how-to/schema)

## Request

## Request URL

https://yuuvis.azure-api.net/admin/schema

## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

## Responses

## 200 OK

### OK

## Representations

`application/xml`

### Sample

```
 <schema>{
  "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
  "xsi:schemaLocation": "http://optimal-systems.org/ns/dmscloud/schema/v4.0/ dmsCloud-schema.xsd",
  "propertyStringDefinition": {
    "id": "myname",
    "propertyType": "string",
    "cardinality": "single",
    "required": true
  },
  "propertyDateTimeDefinition": {
    "id": "mydate",
    "propertyType": "datetime",
    "cardinality": "single",
    "required": true
  },
  "typeDocumentDefinition": {
    "id": "mydocument",
    "baseId": "enaio:document",
    "propertyReference": [
      "myname",
      "mydate"
    ],
    "contentStreamAllowed": "required"
  }
}</schema>

```
### Schema

```
Sample
Schema
 {
  "title": "Tenant Schema Example",
  "required": [
    "propertyStringDefinition",
    "typeDocumentDefinition"
  ],
  "type": "object",
  "properties": {
    "xmlns:xsi": {
      "type": "string",
      "xml": {
        "attribute": true
      }
    },
    "xsi:schemaLocation": {
      "type": "string",
      "xml": {
        "attribute": true
      }
    },
    "propertyStringDefinition": {
      "title": "Property Definition Object",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "propertyType": {
          "type": "string"
        },
        "cardinality": {
          "type": "string"
        },
        "required": {
          "type": "boolean"
        }
      }
    },
    "propertyDateTimeDefinition": {
      "title": "Property Definition Object",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "propertyType": {
          "type": "string"
        },
        "cardinality": {
          "type": "string"
        },
        "required": {
          "type": "boolean"
        }
      }
    },
    "typeDocumentDefinition": {
      "title": "Type Document Definition Object",
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "baseId": {
          "type": "string"
        },
        "propertyReference": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "contentStreamAllowed": {
          "type": "string"
        }
      }
    }
  },
  "xml": {
    "name": "schema",
    "namespace": "http://optimal-systems.org/ns/dmscloud/schema/v4.0/"
  },
  "example": {
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xsi:schemaLocation": "http://optimal-systems.org/ns/dmscloud/schema/v4.0/ dmsCloud-schema.xsd",
    "propertyStringDefinition": {
      "id": "myname",
      "propertyType": "string",
      "cardinality": "single",
      "required": true
    },
    "propertyDateTimeDefinition": {
      "id": "mydate",
      "propertyType": "datetime",
      "cardinality": "single",
      "required": true
    },
    "typeDocumentDefinition": {
      "id": "mydocument",
      "baseId": "enaio:document",
      "propertyReference": [
        "myname",
        "mydate"
      ],
      "contentStreamAllowed": "required"
    }
  }
}
```

## 403 Forbidden

### Forbidden

### Code samples
[Get Raw Tenant Schema](./get-Raw-Tenant-Schema-to-yuuvis.py)