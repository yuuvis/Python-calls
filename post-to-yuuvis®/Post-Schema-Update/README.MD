# Configuration and Settings

## Update the tenant schema

The **"Update the tenant schema"** endpoint validates your schema first, before overwriting your previous schema with it. If the schema is not valid, no update takes place.


[Learn about yuuvis® API schemas](https://yuuvis.io/how-to/schema)

## Request URL

https://api.yuuvis.io/admin/schema

## Request headers

```
Content-Type                        string          application/xml

------------------------------------------------------------------------------------------------------------------------------------

Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

The Schema you are trying to upload to yuuvis, in XML Format.

## Responses

## 200 OK

### OK - Schema is valid

## Representations

`application/json`

### Sample
```
 {
  "validationErrors": []
}
422 Unprocessable Entity
Unprocessable Entity - Schema not valid
```
### Schema
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

## Representations

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
### Schema
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


### Code samples


[Update the tenant schema](./Post-Schema-Update.py)
