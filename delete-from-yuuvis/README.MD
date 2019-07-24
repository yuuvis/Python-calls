# Core Capabilities (CRUD)

### API change history

[Documentation](https://yuuvis.io//how-to)


## Delete document by ID

Already imported documents using the "Store one or more documents" endpoint can be deleted again. 
The **"Delete document by ID"** endpoint offers the functionality to delete the document (object) that matches the given objectId parameter.


[Read about Deleting Documents with the yuuvis® API](https://yuuvis.io/how-to/delete)

[Try It](https://yuuvis.io/docs/services/yuuvis-dms-core/operations/ObjectsByObjectIdDelete/console)
## Request

### Request URL

https://api.yuuvis.io/dms/objects/{objectId}

## Request parameters

```
objectId            string          The objectId of the document (object) to be deleted.

```
## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Request body

## Responses

## 200 OK

### OK - The stored document (object) with this objectId has been deleted.

## 404 Not Found

### Not Found - The document (object) with this objectId can not be found.

## 409 Conflict

### Conflict - The document (object) with this objectId could not be deleted due to retention.

### Code samples

[Delete document by ID](./Delete-from-yuuvis.py)