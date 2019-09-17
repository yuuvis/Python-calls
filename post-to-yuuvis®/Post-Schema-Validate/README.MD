# Configuration and Settings

## Validate a schema

The **"Validate a schema"** endpoint validates a schema and returns a list of validation error messages, if any occur.

[Learn about yuuvis® API schemas](https://yuuvis.io/how-to/schema)

### Request URL

https://api.yuuvis.io/admin/schema/validate

## Request headers

```
Content-Type                        string          application/xml

--------------------------------------------------------------------------------------------------------------------------------

Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

The Schema you are trying to validate, in XML Format.

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

[Validate a schema](./Post-Schema-Validate.py)
