# Core Capabilities (CRUD)

## Delete document version by ID and version number

Imported documents can have multiple versions through content or metadata updates.
Any given version of a document can be deleted by specifiying a version number through a suffix of '/version/{versionNr}' after the objectId. After deleting an older version of a document, the current version as well as other version entries will remain available.
One thing to look out for here is that the API treats the deletion of the current version of a document as a regular deletion, making any of the previous versions unavailable as well. To 'undo' an update, it's advised to pull the previous state (current version number -1) of content or metadata and update the object with those files, then delete the specific version in which the faulty content or metadata resides. This avoids completely removing the object from the registry.
The **"Delete document version by ID"** endpoint offers the functionality to delete the version that matches the given versionNumber parameter of the document (object) that matches the given objectId parameter.


[Read about Deleting Documents with the yuuvis® API](https://yuuvis.io/how-to/delete)

## Request URL

https://api.yuuvis.io/dms/objects/{objectId}/versions/{versionNr}

## Request headers

```
Ocp-Apim-Subscription-Key           string          Subscription key which provides access to this API. Found in your Profile.

```

## Responses

## 200 OK

### OK - The stored document (object) version with this objectId and version number has been deleted.

## 404 Not Found

### Not Found - The document (object) version with this objectId and version number can not be found.

## 409 Conflict

### Conflict - The document (object) version with this objectId and version number could not be deleted due to retention.

### Code samples

[Delete document by ID](./Delete-Object-Version.py)
