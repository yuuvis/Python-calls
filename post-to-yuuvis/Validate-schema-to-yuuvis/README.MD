# Configuration and Settings

### API change history

[Documentation](https://yuuvis.io/how-to)


## Validate a schema

The **"Validate a schema"** endpoint validates a schema and returns a list of validation error messages, if any. Note that the "Try it" button is not available for this endpoint. You have to try it out externally. Use the provided code samples as a starting point.

[Learn about yuuvis® API schemas](https://yuuvis.io/how-to/schema)

## Request

### Request URL

https://api.yuuvis.io/admin/schema/validate

## Request headers

```
Content-Type (optional)             string          Media type of the body sent to the API.

--------------------------------------------------------------------------------------------------------------------------------

Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

`multipart/form-data`

## Responses

### 200 OK                          

### OK - The schema is valid.      

## Representations

`application/json`

## Sample
```
 {
  "validationErrors": []
}

```
## Schema
```
{
  "title": "Validation Error List",
  "type": "object",
  "properties": {
    "validationErrors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "message": {
            "type": "string"
          }
        }
      }
    }
  },
  "example": {
    "validationErrors": []
  }
}
```
## 422 Unprocessable Entity

### Unprocessable Entity - The schema is invalid.

### Representations

`application/json`

### Sample
```
 {
  "validationErrors": [
    {
      "message": "There are 2 property type definitions with the id 'tenNyc999:string3'."
    },
    {
      "message": "Invalid property reference 'string5' in type definition 'tenNyc999:doc2'."
    }
  ]
}
```

## Schema
```

{
  "title": "Validation Error List",
  "type": "object",
  "properties": {
    "validationErrors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "message": {
            "type": "string"
          }
        }
      }
    }
  },
  "example": {
    "validationErrors": [
      {
        "message": "There are 2 property type definitions with the id 'tenNyc999:string3'."
      },
      {
        "message": "Invalid property reference 'string5' in type definition 'tenNyc999:doc2'."
      }
    ]
  }
}
```
## Code samples

[Validate a schema](./Validate-schema-to-yuuvis.py)